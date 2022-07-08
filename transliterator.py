states = ['SPACE', 'INT', 'IDENT', 'ERROR', 'HEX']
operators = ['+', '-', '*', '/', 'div', 'mod']
simple_comparators = ['=', '<', '>']
hex_letters = ['a', 'b', 'c', 'd', 'e', 'f']


def transliterate(data: str) -> list:
    state = 'SPACE'
    lexemes = []
    for char in data:
        match state:
            case 'SPACE':
                if char.isalpha() and char.lower() in hex_letters:
                    state = 'IDENT'
                    lexemes.append((char, 'HEX_LETTER'))
                elif char.isalpha():
                    state = 'IDENT'
                    lexemes.append((char, 'LETTER'))
                elif char.isdigit():
                    state = 'INT'
                    lexemes.append((char, 'DIGIT'))
                elif char == ' ':
                    state = 'SPACE'
                    lexemes.append((char, 'SPACE'))
                elif char in simple_comparators:
                    state = 'SPACE'
                    lexemes.append((char, 'COMPARATOR'))
                elif char in operators:
                    state = 'SPACE'
                    lexemes.append((char, 'OPERATOR'))
                elif char == ';':
                    state = 'SPACE'
                    lexemes.append((char, 'SEMICOLON'))
                elif char == '$':
                    state = 'HEX'
                    lexemes.append((char, 'HEX_SIGN'))
                elif char == ')':
                    state = 'SPACE'
                    lexemes.append((char, 'RIGHT_BR'))
                else:
                    state = 'ERROR'
            case 'INT':
                if char.isalpha():
                    state = 'ERROR'
                elif char.isdigit():
                    state = 'INT'
                    lexemes.append((char, 'DIGIT'))
                elif char == ' ':
                    state = 'SPACE'
                    lexemes.append((char, 'SPACE'))
                elif char in simple_comparators:
                    state = 'SPACE'
                    lexemes.append((char, 'COMPARATOR'))
                elif char in operators:
                    state = 'SPACE'
                    lexemes.append((char, 'OPERATOR'))
                elif char == ';':
                    state = 'SPACE'
                    lexemes.append((char, 'SEMICOLON'))
                elif char == ')':
                    state = 'SPACE'
                    lexemes.append((char, 'RIGHT_BR'))
                else:
                    state = 'ERROR'
            case 'IDENT':
                if char.isalpha() and char.lower() in hex_letters:
                    state = 'IDENT'
                    lexemes.append((char, 'HEX_LETTER'))
                elif char.isalpha():
                    state = 'IDENT'
                    lexemes.append((char, 'LETTER'))
                elif char.isdigit():
                    state = 'IDENT'
                    lexemes.append((char, 'DIGIT'))
                elif char == ' ':
                    state = 'SPACE'
                    lexemes.append((char, 'SPACE'))
                elif char in simple_comparators:
                    state = 'SPACE'
                    lexemes.append((char, 'COMPARATOR'))
                elif char in operators:
                    state = 'SPACE'
                    lexemes.append((char, 'OPERATOR'))
                elif char == ';':
                    state = 'SPACE'
                    lexemes.append((char, 'SEMICOLON'))
                elif char == '(':
                    state = 'SPACE'
                    lexemes.append((char, 'LEFT_BR'))
                elif char == ')':
                    state = 'SPACE'
                    lexemes.append((char, 'RIGHT_BR'))
                else:
                    state = 'ERROR'
            case 'HEX':
                if char.isalpha() and char.lower() in hex_letters:
                    state = 'HEX'
                    lexemes.append((char, 'HEX_LETTER'))
                elif char.isdigit():
                    state = 'HEX'
                    lexemes.append((char, 'HEX_DIGIT'))
                elif char == ' ':
                    state = 'SPACE'
                    lexemes.append((char, 'SPACE'))
                elif char in operators:
                    state = 'SPACE'
                    lexemes.append((char, 'OPERATOR'))
                else:
                    state = 'ERROR'
            case 'ERROR':
                return []
            case _:
                return []
    return lexemes
