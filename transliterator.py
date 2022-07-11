operators = ['+', '-', '*', '/']
simple_comparators = ['=', '<', '>']
hex_letters = ['a', 'b', 'c', 'd', 'e', 'f']

def transliterate(data: str) -> list:
    symbols = []
    for char in data:
        if char.isalpha() and char.lower() in hex_letters:
            symbols.append((char, 'HEX_LETTER'))
        elif char.isalpha():
            symbols.append((char, 'LETTER'))
        elif char.isdigit():
            symbols.append((char, 'DIGIT'))
        elif char == ' ':
            symbols.append((char, 'SPACE'))
        elif char == '(':
            symbols.append((char, 'LEFT_BR'))
        elif char == ')':
            symbols.append((char, 'RIGHT_BR'))
        elif char in simple_comparators:
            symbols.append((char, 'COMPARATOR'))
        elif char in operators:
            symbols.append((char, 'OPERATOR'))
        elif char == '$':
            symbols.append((char, 'HEX_SIGN'))
        elif char == ';':
            symbols.append((char, 'SEMICOLON'))
        else:
            symbols.append((char, 'ERROR'))
            return []
    return symbols
