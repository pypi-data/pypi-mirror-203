import ast
import logging
import os
import re
import traceback

from . import logconf

_CODE_LITERALS = [re.compile(pattern) for pattern in [
    r'\b[a-z]+[A-Z][a-zA-Z]*\b',     # camelCase
    r'\b[A-Z]+_[A-Z]+\b',            # SCREAMING_SNAKE_CASE
    r'\b[A-Za-z]+_\d+[_\d\w]*\b',    # snake_case with numbers
    r'\b[a-z]+_[a-z]+\b',            # snake_case
    r'\b[a-zA-Z]+(?:_[a-zA-Z]+)+\b', # snake_case_long
    r'\b[A-Z][a-zA-Z]*[A-Z]\b',      # PascalCase
    r'\b_[a-zA-Z_]+\b',              # _private
    r'\b__[a-zA-Z_]+__\b',           # __magic__
]]

def _split_py(contents):
    tree = ast.parse(contents)
    results = []

    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            results.append(ast.unparse(node))
        elif isinstance(node, ast.ClassDef):
            results.append(ast.unparse(node))

    return results

def _find_level_n_braces(s, n):
    stack = []
    n_level_braces = []
    for i, c in enumerate(s):
        if c == '{':
            stack.append(i)
        elif c == '}':
            if len(stack) == n:
                n_level_braces.append((stack[-1], i))
            stack.pop()

    return n_level_braces

def _find_line_start(s, i):
    index = s.rfind('\n', 0, i)
    if index == -1:
        index = 0
    else:
        index += 1
    return index

def _find_opening_paren(string, i):
    if string[i] != ')':
        return None

    depth = 0
    for j in range(i-1, -1, -1):
        if string[j] == ')':
            depth += 1
        elif string[j] == '(':
            if depth == 0:
                return j
            else:
                depth -= 1

    return None

def _gcl(string, index): # get containing line debug method
    start_of_line = string.rfind('\n', 0, index) + 1
    end_of_line = string.find('\n', index)
    if end_of_line == -1:
        end_of_line = len(string)

    line = string[start_of_line:end_of_line]
    return line

def _find_last_paren(string, i):
    while i >= 0:
        if string[i] == ')':
            return i
        i -= 1

    return None

def _find_signature_start(code, i):
    try:
        closing = _find_last_paren(code, i)
        opening = _find_opening_paren(code, closing)
        return _find_line_start(code, opening)
    except: # try to dodge parsing errors
        logging.warn(f"failed to parse signature near index {i} in block {code}")
        return None

def _split_bracelang_class(block):
    # TODO improve class splitting for js
    is_class = "class" in block.splitlines()[0]
    if not is_class:
        return [block]

    brace_locs = _find_level_n_braces(block, 2)
    func_locs = [(_find_signature_start(block, start), end) \
        for start, end in brace_locs]

    funcs = []
    for start, end in filter(bool, func_locs):
        func = block[start:end + 1]
        funcs.append(func)

    return funcs

def _contains_unmatched_lp(string):
    stack = []
    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return True
            stack.pop()

    return bool(stack)

def _is_parse_junk(code):
    if code.split(' ')[0] == 'import':
        return True
    if len(code.splitlines()) == 1 and \
            code.strip()[-1] == '}' and \
            _contains_unmatched_lp(code):
        return True

    return False

def _split_bracelang(contents):
    blocks = []
    brace_locs = _find_level_n_braces(contents, 1)
    block_locs = [(_find_line_start(contents, start), end) \
        for start, end in brace_locs]

    for start, end in block_locs:
        block = contents[start:end + 1]
        blocks.append(block)

    subblocks = []
    for block in blocks:
        try:
            new = _split_bracelang_class(block)
            for sb in new:
                if _is_parse_junk(sb): # TODO make this cleaner
                    logging.debug(f"filtered parse junk {sb}")
                    continue
                subblocks.append(sb)
        except:
            exc = traceback.format_exc()
            logging.warn(f"Failed to parse block:\n{block}\n\n{exc}")

    return subblocks

def _split_text(contents):
    paragraphs = []
    current_paragraph = ''
    for line in contents.splitlines():
        if line.strip() == '':
            if current_paragraph != '':
                paragraphs.append(current_paragraph.strip())
                current_paragraph = ''
        else:
            current_paragraph += line + '\n'
    if current_paragraph != '':
        paragraphs.append(current_paragraph.strip())
    return paragraphs

def detect_language(string):
    _, ext = os.path.splitext(string)
    ext = ext.lower()
    if ext == '.py':
        return 'python'
    elif ext == '.java':
        return 'java'
    elif ext in ['.c', '.cpp', '.cc', '.cxx', '.h', '.hpp', '.hxx']:
        return 'c/c++'
    elif ext == '.go':
        return 'go'
    elif ext == '.js' or ext == '.mjs':
        return 'javascript'
    elif ext == '.ts':
        return 'typescript'
    elif ext == '.css':
        return 'css'
    elif ext == '.php':
        return 'php'
    elif ext == '.swift':
        return 'swift'
    elif ext == '.sh':
        return 'bash'
    elif ext == '.rs':
        return 'rust'
    elif ext in ['.sc', '.scala']:
        return 'scala'
    # TODO extend language support
    else:
        return None

def split_code(path, content):
    funcs = {
        'c/c++': _split_bracelang,
        'css': _split_bracelang,
        'go': _split_bracelang,
        'java': _split_bracelang,
        'javascript': _split_bracelang,
        'php': _split_bracelang,
        'python': _split_py,
        'rust': _split_bracelang,
        'scala': _split_bracelang,
        'swift': _split_bracelang,
        'typescript': _split_bracelang,
    }

    lang = detect_language(path)
    logging.info(f"detected {lang}")
    splitter = funcs.get(lang, _split_text)

    return splitter(content)

def extract_code_literals(text):
    literals = []
    for regex in _CODE_LITERALS:
        matches = re.findall(regex, text)
        if matches:
            literals.extend(matches)

    return set(literals)
