states = ['SPACE', 'INT', 'IDENT', 'HEX']
operators = ['+', '-', '*', '/', 'div', 'mod']
simple_comparators = ['=', '<', '>']


def transliterate(data: str) -> list:
    state = 'SPACE'
    lexemes = []
    for char in data:
        if state == 'SPACE':
            if char.isdigit():
                state = 'INT'
                lexemes.append((char, 'digit'))
            elif char.isalpha():
                state = 'IDENT'
                lexemes.append((char, 'letter'))
            elif char == ';':
                state = 'SPACE'
                lexemes.append((char, 'semicolon'))
            elif char == ' ':
                lexemes.append((char, 'space'))
                state = 'SPACE'
            elif char == '(':
                state = 'SPACE'
                lexemes.append((char, 'lpar'))
            elif char == ')':
                state = 'SPACE'
                lexemes.append((char, 'rpar'))
            elif char == '$':
                state = 'HEX'
                lexemes.append((char, 'const_sign'))
            elif char in simple_comparators:
                state = 'SPACE'
                lexemes.append((char, 'comparator'))
            elif char in operators:
                state = 'SPACE'
                lexemes.append((char, 'operator'))
            else:
                return []
        elif state == 'HEX':
            if char.isdigit():
                lexemes.append((char, 'hex_digit'))
            elif char.isalpha() and char.lower() in ['a', 'b', 'c', 'd', 'e', 'f']:
                lexemes.append((char, 'hex_digit'))
            elif char == ' ':
                lexemes.append((char, 'space'))
                state = 'SPACE'
            elif char in ['+', '-', '*', '/']:
                lexemes.append((char, 'operator'))
                state = 'SPACE'
            else:
                return []
        elif state == 'INT':
            if char.isalpha():
                return []
            elif char.isdigit():
                state = 'INT'
                lexemes.append((char, 'digit'))
            elif char == '(':
                state = 'SPACE'
                lexemes.append((char, 'lpar'))
            elif char == ' ':
                state = 'SPACE'
                lexemes.append((char, 'space'))
            elif char == ';':
                state = 'SPACE'
                lexemes.append((char, 'semicolon'))
            elif char == ')':
                state = 'SPACE'
                lexemes.append((char, 'rpar'))
            elif char == '$':
                state = 'HEX'
                lexemes.append((char, 'const_sign'))
            elif char in simple_comparators:
                return []
            elif char in operators:
                state = 'SPACE'
                lexemes.append((char, 'operator'))
            else:
                return []
        elif state == 'IDENT':
            if char.isdigit():
                state = 'IDENT'
                lexemes.append((char, 'digit'))
            elif char.isalpha():
                state = 'IDENT'
                lexemes.append((char, 'letter'))
            elif char == ';':
                state = 'SPACE'
                lexemes.append((char, 'semicolon'))
            elif char == ' ':
                state = 'SPACE'
                lexemes.append((char, 'space'))
            elif char == '(':
                state = 'SPACE'
                lexemes.append((char, 'lpar'))
            elif char == ')':
                state = 'SPACE'
                lexemes.append((char, 'rpar'))
            elif char == '$':
                state = 'SPACE'
                lexemes.append((char, 'const_sign'))
            elif char in simple_comparators:
                state = 'SPACE'
                lexemes.append((char, 'comparator'))
            elif char in operators:
                state = 'SPACE'
                lexemes.append((char, 'operator'))
            else:
                return []
    return lexemes
