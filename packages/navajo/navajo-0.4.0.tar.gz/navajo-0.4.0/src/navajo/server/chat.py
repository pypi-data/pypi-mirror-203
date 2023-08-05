import logging
import numpy as np
import traceback

from . import api
from . import database
from . import index
from . import logconf
from .dependency import find_dependencies
from .prompt import load_prompt
from .split import extract_code_literals, split_code
from .vector import cosine_sim, unique_elements

CONTEXT_MSG_BYTE_CAP = 35000
TOKEN_LIMIT = 4096

class WeightedMessage(object):
    def __init__(self, role, content, weight=1.0, split=False, source=None):
        self.role = role
        self.content = content
        self.weight = weight
        self.split = split
        self.source = source

    def to_dict(self):
        return {'role': self.role, 'content': self.content}

def _needs_context(query, messages):
    # TODO implement context need determination
    return True

def _get_msg_embeddings(messages, user, project_id):
    retrieved = {}
    to_embed = []

    for m in messages:
        if m.source and not m.split:
            try:
                e = index.retrieve_embedding(m.source, user, project_id)
                logging.debug(f'retrieved vector for file {m.source}')
                retrieved[m.content] = e
            except:
                logging.warning(traceback.format_exc())
                to_embed.append(m.content)
        else:
            to_embed.append(m.content)

    if to_embed:
        embedded = dict(zip(to_embed, api.embed_all(to_embed)))
    else:
        embedded = {}
    return {**retrieved, **embedded}

def _weighted_vec(query_vec, message_vecs):
    # Threshold to only keep reasonably relevant vectors
    history_depth = 16 # TODO determine appropriate value for this
    relevant_vecs = [vec for vec in message_vecs[:history_depth] if cosine_sim(query_vec, vec) >= 0.7]

    weights = []
    for vec in relevant_vecs:
        sim = cosine_sim(query_vec, vec)
        # Map similarity to 0-1 range using sigmoid
        weight = 1 / (1 + np.exp(-sim))
        # Apply exponential weighting) with bias
        weight = weight ** 2
        weights.append(weight)

    if not weights:
        return query_vec

    # Always give query vector the highest weight
    weights[0] = max(weights)

    # Average the top 3-5 vectors to construct the final context vector
    context_vec = weights[0] * np.array(query_vec)
    for i in range(1, min(len(weights), 5)):
        context_vec += weights[i] * np.array(relevant_vecs[i])

    # TODO do some logging to test the quality of this implementation
    return context_vec.tolist()

def _get_context_vector(query, messages, user, project_id):
    all_msg = [WeightedMessage('user', query), *messages]
    vectors = _get_msg_embeddings(all_msg, user, project_id)
    query_vec = vectors[query]
    del vectors[query]

    return _weighted_vec(query_vec, list(vectors.values()))

def _split_file(path, content, context_vector):
    all_blocks = split_code(path, content)
    vectors = dict(zip(all_blocks, api.embed_all(all_blocks)))
    sorted_blocks = iter(sorted(all_blocks,
        key=lambda b: cosine_sim(context_vector, vectors[b])))

    blocks = []
    block_bytes = 0
    while block_bytes < CONTEXT_MSG_BYTE_CAP:
        try:
            block = next(sorted_blocks)
        except StopIteration:
            break
        blocks.append(block)

    return blocks

def _get_literally_relevant(query, user, project_id):
    literals = extract_code_literals(query)
    if not literals:
        return []
    logging.debug(f"Found literals in query: {literals}")

    conn = database.get_connection('projects')
    c = conn.cursor()

    file_matches = {}
    for literal in literals:
        # Search for files containing the literal in the keyword_index table
        c.execute('''
            SELECT file_path
            FROM keyword_index
            WHERE user_id = ? AND project_id = ? AND keyword = ?
        ''', (user, project_id, literal))

        files_with_literal = [row[0] for row in c.fetchall()]
        for file in files_with_literal:
            if file in file_matches:
                file_matches[file] += 1
            else:
                file_matches[file] = 1

    c.close()
    database.close_connection('projects', conn)

    sorted_files = sorted(file_matches.items(), key=lambda x: x[1], reverse=True)
    logging.debug(f"Query <{query}> literally matched files: {sorted_files}")
    return [file for file, matches in sorted_files]

def _inject_context(query, messages, user, project_id):
    context_vec = _get_context_vector(query, messages, user, project_id)

    # Embedding similarity
    top_files = [f for (f, _) in index.search(context_vec, user, project_id)[:3]]
    logging.debug(f'top_files={top_files}')

    # Literal code token match
    literal_files = _get_literally_relevant(query, user, project_id)[:3]
    logging.debug(f'literal_files={literal_files}')

    # Dependencies and dependants of relevant files
    possible_deps = []
    for f in (top_files + literal_files):
        possible_deps.extend(find_dependencies(f, user, project_id))
    dependency_files = [f for (f, _) in index.search(context_vec, user, project_id, file_set=possible_deps)[:3]]
    logging.debug(f'dep_files={dependency_files}')

    def _get_weight(file):
        weight = 1.0
        if file in literal_files:
            weight += 0.15
        if file in dependency_files:
            weight += 0.1
        return weight

    # TODO weight files based on recurrence instead of using set
    all_relevant_files = unique_elements(top_files + literal_files + dependency_files)
    logging.debug(f'relevant files: {all_relevant_files}')

    for file in reversed(all_relevant_files):
        content = index.get_file(file, user, project_id)
        split_blocks = False
        if len(content) > CONTEXT_MSG_BYTE_CAP:
            blocks = _split_file(file, content, context_vec)
            split_blocks = True
        else:
            blocks = [content]
        for block in blocks:
            prompt_name = 'ack_block' if split_blocks else 'ack_code'
            block_msg = load_prompt(prompt_name).format(file_path=file, code=block)
            weight = _get_weight(file)
            messages.append(WeightedMessage('user', block_msg, weight=weight, split=split_blocks, source=file))
            messages.append(WeightedMessage('assistant', 'okay', weight=0.5))

def _msg_tokens(q, m, o):
    s = ' '.join(x.content for x in m) + ' ' + q
    return api.count_tokens(s) + o

def _reduce_context(query, messages, user, project_id, out_tokens):
    out_tokens += api.count_tokens(load_prompt('system_query'))
    context_vec = _get_context_vector(query, messages, user, project_id)
    messages_content = [m.content for m in messages]
    msg_embeddings = _get_msg_embeddings(messages, user, project_id)

    def _relevance(message):
        msg_vec = msg_embeddings[message.content]
        # logging.debug(f'calculate relevance of {message.content}')
        return cosine_sim(context_vec, msg_vec) * message.weight

    relevance_index = sorted([[i, _relevance(m)] for (i, m) in enumerate(messages)], key=lambda p: p[1])
    logging.debug(f'current max relevance = {relevance_index[-1]}')

    while _msg_tokens(query, messages, out_tokens) > api.MAX_CHAT_TOKENS:
        if len(messages) == 1:
            logging.error('Encountered irreducible context (message length of 1)')
            raise ValueError('Context too large!')

        # TODO alternatively, instead of removing the least relevant, when the
        # message stack reaches 3 messages, we could begin splitting files into
        # blocks and removing the least relevant blocks

        i_remove, score = relevance_index.pop(0)
        msg_to_remove = messages[i_remove].content
        logging.debug(f"low score {score} - reducing context by deleting message <{msg_to_remove}>")

        messages.pop(i_remove)
        for i in range(len(relevance_index)):
            if relevance_index[i][0] > i_remove:
                relevance_index[i][0] -= 1

def get_response(query, msgs, user, project_id, n_retries=0):
    msgs = [WeightedMessage(**m) for m in msgs] # TODO introduce source=chat
    if _needs_context(query, msgs):
        _inject_context(query, msgs, user, project_id)

    tokens_out = 750
    args = {
        'max_tokens': tokens_out,
        'n': 1,
        'stop': None,
        'temperature': 0.5,
    }

    retries = 3
    response = None
    while retries:
        logging.debug(f'msgs is currently {[m.content for m in msgs]}')
        _reduce_context(query, msgs, user, project_id, tokens_out + ((3 - retries)* 200))
        try:
            sent_msgs = [msg.to_dict() for msg in msgs]
            sent_msgs.insert(0, {'role': 'system', 'content': load_prompt('system_query')})
            sent_msgs.append({'role': 'user', 'content': query})
            response = api.open_stream(sent_msgs, args)
            break

        except:
            logging.error("Failed to send messages to completion API:\n" + traceback.format_exc())
            logging.info(f"_msg_tokens reports {_msg_tokens(query, msgs, tokens_out)} tokens")
            logging.info("retrying get_response")
            retries -= 1

    api.log_call_count()
    return response
