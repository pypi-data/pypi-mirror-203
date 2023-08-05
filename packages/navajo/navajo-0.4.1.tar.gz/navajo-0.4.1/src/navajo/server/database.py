import logging
import os
import sqlite3

from . import logconf

def _build_db_path(db_name):
    home = os.path.expanduser("~")
    db_path = os.path.join(home, ".config", "navajo", "db", f"{db_name}.db")
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    return db_path

def get_connection(db_name):
    db_path = _build_db_path(db_name)
    return sqlite3.connect(db_path)

def close_connection(db_name, conn): # TODO refactor this out
    conn.close()

def init_embedding_db():
    conn = get_connection('embeddings')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS embeddings '
              '(hash TEXT PRIMARY KEY, embedding TEXT)')
    conn.commit()
    c.close()
    close_connection('embeddings', conn)

def init_project_db():
    conn = get_connection('projects')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS keyword_index (
        user_id TEXT,
        project_id TEXT,
        keyword TEXT,
        file_path TEXT
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS metadata (
        user_id TEXT,
        project_id TEXT,
        created_time TIMESTAMP,
        project_path TEXT,
        index_id TEXT,
        version TEXT
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS file_index (
        user_id TEXT,
        project_id TEXT,
        file_path TEXT,
        embedding TEXT
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS dependency_graph (
        user_id TEXT,
        project_id TEXT,
        file_path TEXT,
        dependencies TEXT,
        dependants TEXT
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS file_hashes (
        user_id TEXT NOT NULL,
        project_id TEXT NOT NULL,
        file_path TEXT NOT NULL,
        file_hash TEXT NOT NULL,
        PRIMARY KEY (user_id, project_id, file_path)
    )''')

    conn.commit()
    c.close()
    close_connection('projects', conn)
