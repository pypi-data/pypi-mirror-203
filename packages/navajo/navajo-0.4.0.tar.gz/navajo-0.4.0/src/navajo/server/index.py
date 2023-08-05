import cachetools
import concurrent.futures
import hashlib
import json
import logging
import os
import time
import traceback
import uuid

from . import database
from . import logconf
from .api import get_embedding
from .dependency import build_dependency_graph
from .split import extract_code_literals
from .vector import cosine_sim

from datetime import datetime
from functools import lru_cache, partial

INDEX_CACHE = cachetools.TTLCache(maxsize=64, ttl=300)
database.init_project_db()

def _summarize_file(pair):
    file_path, contents = pair
    if len(contents) > (50 * 1024 ** 2):
        logging.warning(f"Ignoring huge (>50MB) file {file_path}")
        return None

    embedding = get_embedding(contents) # TODO rewrite to use embed_all
    literals = extract_code_literals(contents)
    entry = {
        'embedding': [round(x, 8) for x in embedding],
        'file_path': file_path,
        'literals': literals,
    }

    return file_path, entry

def _rel_path(path, parent):
    path = os.path.normpath(path)
    parent = os.path.normpath(parent)

    path_parts = path.split(os.path.sep)
    parent_parts = parent.split(os.path.sep)
    if not path.startswith(parent):
        raise ValueError(f"{parent} is not a prefix of {path}")

    common_parts = os.path.commonprefix([path_parts, parent_parts])
    num_common = len(common_parts)
    num_parent_parts = len(parent_parts)
    num_rel_parts = len(path_parts) - num_common
    rel_parts = [".."] * (num_parent_parts - num_common) + path_parts[num_common:]
    rel_path = os.path.join(*rel_parts)

    return rel_path

def _generate_index(files, project_path):
    len_files = len(files)
    counter = {'n_complete': 0}
    job_id = uuid.uuid4()

    def _summarize_file_with_logging(counter, file_contents):
        result = _summarize_file(file_contents)
        counter['n_complete'] += 1
        if counter['n_complete'] % 10 == 0:
            logging.info(f"indexing job {job_id} progress: {counter['n_complete']} / {len_files}")
        return result

    with concurrent.futures.ThreadPoolExecutor() as executor:
        func = partial(_summarize_file_with_logging, counter)
        index = filter(bool, executor.map(func, files.items()))

    return dict(index)

def get_file(file, user, project_id):
    conn = database.get_connection('projects')
    c = conn.cursor()
    c.execute('SELECT project_path FROM metadata WHERE user_id=? AND project_id=?', (user, project_id))
    result = c.fetchone()
    if result is None:
        raise FileNotFoundError(f"Project path not found for user {user} and project_id {project_id}")

    project_path = result[0]
    local_file_path = os.path.join(project_path, file)

    try:
        with open(local_file_path, 'r') as f:
            content = f.read()
    except:
        tb = traceback.format_exc()
        logging.error(f"{user} {project_id} Failed to retrieve project file with local path {local_file_path}\n{tb}")
        raise FileNotFoundError

    return content

def _measure_files(files):
    total_size = sum(len(content) for content in files.values()) / (1024 * 1024)
    logging.debug(f'Total size of all files: {total_size:.2f} MB')
    return total_size

def _update_project_files(files, user, project_id):
    conn = database.get_connection('projects')
    c = conn.cursor()
    c.execute('SELECT file_path FROM file_hashes WHERE user_id=? AND project_id=?', (user, project_id))
    existing_files = set([row[0] for row in c.fetchall()])
    new_files = set(files.keys())
    files_to_delete = existing_files - new_files

    for path in files_to_delete:
        c.execute('DELETE FROM file_hashes WHERE user_id=? AND project_id=? AND file_path=?',
                  (user, project_id, path))

    conn.commit()
    c.close()
    database.close_connection('projects', conn)

def create(files, user, project_path, project_id=None): # TODO update incrementally
    if _measure_files(files) > 500:
        raise ValueError('Input too large.')

    if not project_id:
        project_id = str(uuid.uuid4())

    logging.info(f'Starting indexing job for user {user} on project {project_id}: {len(files)} files')
    files = {_rel_path(f, project_path): contents for (f, contents) in files.items()}

    _update_project_files(files, user, project_id)
    file_data = _generate_index(files, project_path)
    index_id = str(uuid.uuid4())

    # Clear existing indexes
    conn = database.get_connection('projects')
    c = conn.cursor()

    tables = ['metadata', 'file_index', 'keyword_index', 'dependency_graph']
    for table in tables:
        query = f'DELETE FROM {table} WHERE user_id=? AND project_id=?'
        c.execute(query, (user, project_id))

    # Save index data to project tables
    c.execute('INSERT INTO metadata VALUES (?, ?, ?, ?, ?, ?)',
              (user, project_id, datetime.now(), project_path, index_id, '0.0.1'))

    for file_path, data in file_data.items():
        c.execute('INSERT INTO file_index VALUES (?, ?, ?, ?)',
                  (user, project_id, file_path, json.dumps(data['embedding'])))

    # Insert keywords and their file paths into the keyword_index table
    for file_path, data in file_data.items():
        keywords = data.get('literals', [])
        for keyword in keywords:
            c.execute('''
                INSERT INTO keyword_index (user_id, project_id, keyword, file_path)
                VALUES (?, ?, ?, ?)
            ''', (user, project_id, keyword, file_path))

    # Build and save dependency graph
    dependency_graph = build_dependency_graph(files)
    for file_path, links in dependency_graph.items():
        dependencies = json.dumps(list(links['dependencies']))
        dependants = json.dumps(list(links['dependants']))
        c.execute('''INSERT INTO dependency_graph (user_id, project_id, file_path, dependencies, dependants)
                     VALUES (?, ?, ?, ?, ?)''',
                     (user, project_id, file_path, dependencies, dependants))

    conn.commit()
    c.close()
    database.close_connection('projects', conn)

    _clear_index_cache(user, project_id)
    logging.info(f'Saved a new index: {index_id}')

    return project_id

def _clear_index_cache(user, project_id):
    global INDEX_CACHE
    key = (user, project_id)
    try:
        del INDEX_CACHE[key]
    except KeyError:
        logging.info(f'tried to clear nonexistent cache entry {key}')

def _load_index(user, project_id):
    global INDEX_CACHE
    cache_key = (user, project_id)
    if cache_key in INDEX_CACHE:
        return INDEX_CACHE[cache_key]

    conn = database.get_connection('projects')
    c = conn.cursor()
    c.execute("SELECT file_path, embedding FROM file_index WHERE user_id=? AND project_id=?",
        (user, project_id))

    # TODO why is `embedding` of type `memoryview` in prod?
    result = c.fetchall()
    try:
        index = {file_path: json.loads(embedding) for file_path, embedding in result}
    except AttributeError:
        index = {file_path: embedding for file_path, embedding in result}
    logging.debug(f"{user} | {project_id} found {len(index)} files")

    c.close()
    database.close_connection('projects', conn)

    INDEX_CACHE[cache_key] = index
    return index

def retrieve_embedding(file_path, user, project_id):
    conn = database.get_connection('projects')
    c = conn.cursor()
    c.execute("SELECT embedding FROM file_index WHERE user_id=? AND project_id=? AND file_path=?",
        (user, project_id, file_path))

    result = c.fetchone()
    c.close()
    database.close_connection('projects', conn)

    data = result[0]
    return json.loads(data)

def search(query_embedding, user, project_id, file_set=None):
    index = _load_index(user, project_id)
    if isinstance(query_embedding, str):
        query = query.strip()
        query_embedding = get_embedding(query)

    similarity = {}
    for file_path, file_embedding in index.items():
        if file_set and file_path not in file_set:
            continue
        if not file_embedding:
            continue
        print('content', query_embedding, '\n', file_embedding)
        print('types', type(query_embedding), type(file_embedding))
        similarity[file_path] = cosine_sim(query_embedding, file_embedding)

    return list(sorted(similarity.items(), key=lambda x: x[1], reverse=True))

# TODO should probably delete this function - mostly for testing
def update_keywords(files, user, project_path, project_id=None):
    if _measure_files(files) > 250:
        raise ValueError('Input too large.')

    logging.info(f'Starting keyword update job for user {user} on project {project_id}: {len(files)} files')
    files = {_rel_path(f, project_path): contents for (f, contents) in files.items()}

    conn = database.get_connection('projects')
    c = conn.cursor()
    c.execute('DELETE FROM keyword_index WHERE user_id=? AND project_id=?', (user, project_id))
    literals = {path: extract_code_literals(contents) for path, contents in files.items()}

    for (file_path, keywords) in literals.items():
        for keyword in keywords:
            c.execute('''
                INSERT INTO keyword_index (user_id, project_id, keyword, file_path)
                VALUES (?, ?, ?, ?)
            ''', (user, project_id, keyword, file_path))

    conn.commit()
    c.close()
    database.close_connection('projects', conn)
    logging.info(f'Keywords updated for project {user}_{project_id}')
    return project_id
