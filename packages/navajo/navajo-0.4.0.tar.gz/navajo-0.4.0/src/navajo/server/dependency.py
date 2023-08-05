import json
import logging
import os
import re

from . import database
from . import logconf
from .split import detect_language

from collections import defaultdict

def map_dependencies(deps, files):
    local_dependencies = []

    def find_matching_file(dep, files):
        dep_patterns = [
            re.escape(dep).replace('\\.', '/'),
            re.escape(dep).replace('\\.', '\\\\')  # For languages that use '.' as a separator
        ]
        for file_path in files:
            for pattern in dep_patterns:
                if re.search(fr'{pattern}\.\w+$', file_path):
                    return file_path
        return None

    for dep in deps:
        matched_file = find_matching_file(dep, files)
        if matched_file:
            local_dependencies.append(matched_file)

    return local_dependencies

# TODO need to better test and support non python languages
def extract_dependencies(file_path, file_contents):
    dependency_patterns = {
        'python': [
            r'(?:(?:import\s+(\w+))|(?:from\s+(\w+)\s+import))',
            r'from (.*) import ([A-z]*)',
        ],
        'javascript': r'import(?:\s+\w+\s+)?from\s+[\'"](.+?)[\'"]',
        'typescript': r'import(?:\s+\w+\s+)?from\s+[\'"](.+?)[\'"]',
        'c/c++': r'#include\s+[<"](.+?)[">]',
        'ruby': r'require\s*\(\s*[\'"](.+?)[\'"]\s*\)',
        'php': r'require(?:_once)?\s*\(\s*[\'"](.+?)[\'"]\s*\)',
        'go': r'import\s+(?:\.\s*)?(?:[_\w]+\s+)?"(.+?)"',
        'scala': r'import\s+(?:[_\w]+\.)+[_\w]+(?:\.\{.+?\})?',
        'haskell': r'import\s+(?:qualified\s+)?[_\w]+(?:\s+as\s+[_\w]+)?(?:\s+hiding\s+\((.+?)\))?',
    }

    language = detect_language(file_path)
    patterns = dependency_patterns.get(language)
    if not patterns:
        return set()

    def _handle_match(vals):
        if isinstance(vals, tuple):
            ne_vals = [x for x in vals if x]
        elif isinstance(vals, str):
            ne_vals = [vals]
        count = len(ne_vals)

        if count == 0:
            return [None]
        elif count == 1:
            return ne_vals
        else:
            parts = []
            for val in ne_vals:
                parts.extend(val.split('.'))

            return ['/'.join(p) for p in [parts, parts[:-1]]]

    if not isinstance(patterns, list):
        patterns = [patterns]

    dep_matches = set()
    for pattern in patterns:
        dep_matches.update(re.findall(pattern, file_contents, re.MULTILINE))

    dependencies = []
    for d in dep_matches:
        module_candidates = _handle_match(d)
        if module_candidates:
            dependencies.extend(map(lambda path: re.sub(r'^(\.\/|\.\.\/)*', '', path),
                module_candidates))

    logging.debug(f'file {file_path} matched dependencies {dep_matches}')
    logging.debug(f'cleaned dependencies = {dependencies}')

    return dependencies

def build_dependency_graph(files):
    dependency_graph = defaultdict(set)
    for file_path, contents in files.items():
        logging.info('Process dependencies for file %s', file_path)
        dependencies = extract_dependencies(file_path, contents)
        local_dependencies = map_dependencies(dependencies, files)
        dependency_graph[file_path] = {'dependencies': set(local_dependencies), 'dependants': set()}

    for file_path, file_data in dependency_graph.items():
        for dependency in file_data['dependencies']:
            if dependency in dependency_graph:
                dependency_graph[dependency]['dependants'].add(file_path)

    return dependency_graph

def find_dependencies(file_path, user, project_id):
    conn = database.get_connection('projects')
    c = conn.cursor()
    c.execute('SELECT dependencies, dependants FROM dependency_graph WHERE user_id=? AND project_id=? AND file_path=?',
        (user, project_id, file_path))
    result = c.fetchone()
    c.close()
    database.close_connection('projects', conn)

    if result:
        dependencies, dependants = result
        return [*dependants, *dependencies]
    else:
        return []
