import os
import parse

PROMPT_DIR = './prompts'

def load_prompt(name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    try:
        with open(os.path.join(dir_path, PROMPT_DIR, name + '.txt')) as fp:
            return fp.read()
    except FileNotFoundError:
        msg = f'Couldn\'t find the prompt called "{name}"'
        raise NameError(msg)

def parse_prompt(name, string):
    prompt = load_prompt(name)
    return parse.search(prompt, string)
