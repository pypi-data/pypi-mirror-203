import gzip
import json
import logging
import os
import requests
import signal
import sys
import time
import traceback
import uuid

from . import logconf
from . import index
from .chat import get_response

from flask import Flask, request, Response
from functools import wraps, lru_cache
from sseclient import SSEClient

api = Flask(__name__)
user = "default_user" # TODO clean up

def ttl_cache(ttl):
    def decorator(f):
        @lru_cache(maxsize=None)
        def wrapper(*args, **kwargs):
            result, timestamp = f(*args, **kwargs)
            if time.time() - timestamp > ttl:
                wrapper.cache_clear()
                result, timestamp = f(*args, **kwargs)
            return result

        return wrapper

    return decorator

def generate_sse(stream):
    client = SSEClient(stream)
    for event in client.events():
        new_event = f"event: {event.event}\ndata: {event.data}\n\n"
        yield new_event

@api.route("/respond", methods=["POST"])
def respond():
    data = request.get_json()
    project_id = data.get("project_id")
    logging.debug(f"user / project_id = {user} / {project_id}")

    query = data.get("query")
    messages = data.get("messages")

    stream = get_response(query, messages, user, project_id)
    return Response(generate_sse(stream), content_type='text/event-stream')

@api.route("/index", methods=["POST"])
def create_index():
    if 'Content-Encoding' in request.headers and request.headers['Content-Encoding'] == 'gzip':
        string = gzip.decompress(request.data).decode()
        data = json.loads(string)
    else:
        data = request.get_json()

    files = data['files']
    project_path = data['project_path']
    project_id = data.get('project_id')

    logging.info(f"Received create index request for project {project_path} - {len(files)} files / id {project_id}")

    try:
        project_id = index.create(files, user, project_path, project_id=project_id)
        message, code = "Index created successfully", 200
    except ValueError as e:
        if "too large" in e:
            message, code = "Failed to create index: project exceeded file size limit", 413
        else:
            raise
    except:
        exc_id = uuid.uuid4()
        logging.warning(f'Exception ID {exc_id}\n{traceback.format_exc()}')
        message, code = f"Failed to create index (exception ID: {exc_id})", 503

    return {
        'message': message,
        'project_id': project_id,
    }, code

@api.route('/keywords', methods=['POST'])
def update_keywords():
    if 'Content-Encoding' in request.headers and request.headers['Content-Encoding'] == 'gzip':
        string = gzip.decompress(request.data).decode()
        data = json.loads(string)
    else:
        data = request.get_json()
    files = data['files']
    project_path = data['project_path']
    project_id = data.get('project_id')
    logging.info(f'Received update keywords request for project {project_path} - {len(files)} files / id {project_id}')
    try:
        project_id = index.update_keywords(files, user, project_path, project_id=project_id)
        (message, code) = ('Keywords updated successfully', 200)
    except ValueError as e:
        if 'too large' in e:
            (message, code) = ('Failed to update keywords: project exceeded file size limit', 413)
        else:
            raise
    except:
        exc_id = uuid.uuid4()
        logging.warning(f'Exception ID {exc_id}\n{traceback.format_exc()}')
        (message, code) = (f'Failed to update keywords (exception ID: {exc_id})', 503)
    return ({'message': message, 'project_id': project_id}, code)

# @ttl_cache(5 * 60)
# def _get_latest_cli_version():
#     response = requests.get("https://pypi.org/pypi/codetalk/json")
#     if response.status_code == 200:
#         data = response.json()
#         version = data.get("info", {}).get("version")
#         return version, time.time()
#     else:
#         return None, time.time()

# @api.route("/cli_version", methods=["GET"])
# def cli_version():
#     version = _get_latest_cli_version()
#     if version:
#         return {"version": version}, 200
#     else:
#         return {"error": "Failed to fetch the latest CLI version"}, 500

def main(child=True):
    if child:
        sys.stdout = open(os.devnull, 'w')
        sys.stderr = open(os.devnull, 'w')
        signal.signal(signal.SIGINT, signal.SIG_IGN)

    logging.info("start server")
    api.run(port=20888, debug=False)

if __name__ == '__main__':
    main()
