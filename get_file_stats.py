import re

def get_file_stats(file_path):
    code_lines = 0
    empty_lines = 0
    physical_lines = 0
    logical_lines = 0
    comment_lines = 0
    comment_level = 0
    string_char = None
    in_string = False
    multiline_tokens = []

    str_re = re.compile(r'\"|\'')

    open_tokens_re = re.compile(r'[\[\(\{]')
    close_tokens_re = re.compile(r'[\]\)\}]')
    partial_comment_re = re.compile(r'(.*)#(.*)$')

    comment_re = re.compile(r'\s*#(.*)$')
    blank_re = re.compile(r'^\s*$')


    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            physical_lines += 1

            if blank_re.match(line):
                empty_lines += 1
                continue

            if comment_re.match(line):
                comment_lines += 1
                curr_comment_level = len(line) - len(line.lstrip())
                comment_level = max(comment_level, curr_comment_level)
                continue

            code_lines += 1

            if (str_re.search(line) 
                or open_tokens_re.search(line) 
                or close_tokens_re.search(line)
                or partial_comment_re.search(line)):
                for i, ch in enumerate(line):
                    if str_re.match(ch):
                        if not in_string:
                            string_char = ch
                            in_string = True
                        elif string_char == ch and i > 0 and line[i-1] != '\\':
                            in_string = False
                    
                    if not in_string:
                        if(partial_comment_re.match(ch)):
                            comment_lines += 1
                            curr_comment_level = len(line) - len(line.lstrip())
                            comment_level = max(comment_level, curr_comment_level)
                            break
                        if open_tokens_re.match(ch):
                            multiline_tokens.append(ch)
                        elif close_tokens_re.match(ch):
                            multiline_tokens.pop()
                
                
            if not in_string and len(multiline_tokens) == 0:
                    logical_lines += 1
        return {
            'physical_lines': physical_lines,
            'code_lines': code_lines,
            'logical_lines': logical_lines,
            'empty_lines': empty_lines,
            'comment_lines': comment_lines,
            'comment_level': comment_level
        }
