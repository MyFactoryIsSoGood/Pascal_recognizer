def lex(symbols: list) -> list:
    buffer = {
        'value': '',
        'description': None
    }
    words = []
    state = "SPACE"

    for s in symbols:
        (char, type) = s
        match state:
            case 'SPACE':
                if type in ['LETTER', 'HEX_LETTER']:
                    words.append((buffer['value'], buffer['description']))
                    state = 'IDENT'
                    buffer['value'] = char
                    buffer['description'] = 'IDENT'
                elif type == 'SPACE':
                    state = 'SPACE'
                elif type == 'DIGIT':
                    words.append((buffer['value'], buffer['description']))
                    state = 'INT'
                    buffer['value'] = char
                    buffer['description'] = 'INT'
                elif type == 'HEX_SIGN':
                    words.append((buffer['value'], buffer['description']))
                    state = 'HEX_CONST'
                    buffer['value'] = char
                    buffer['description'] = 'HEX_CONST'
                elif type == 'OPERATOR':
                    words.append((buffer['value'], buffer['description']))
                    state = 'SPACE'
                    buffer['value'] = char
                    buffer['description'] = 'OPERATOR'
                elif type == 'COMPARATOR':
                    words.append((buffer['value'], buffer['description']))
                    state = 'COMPARATOR'
                    buffer['value'] = char
                    buffer['description'] = 'COMPARATOR'
                elif type == 'RIGHT_BR':
                    words.append((buffer['value'], buffer['description']))
                    state = 'SPACE'
                    buffer['value'] = char
                    buffer['description'] = 'RIGHT_BR'
                elif type == 'SEMICOLON':
                    words.append((buffer['value'], buffer['description']))
                    state = 'SPACE'
                    buffer['value'] = char
                    buffer['description'] = 'SEMICOLON'
                else:
                    state = 'ERROR'
            case 'INT':
                if type == 'DIGIT':
                    state = 'INT'
                    buffer['value'] += char
                elif type == 'SPACE':
                    state = 'SPACE'
                elif type == 'OPERATOR':
                    state = 'SPACE'
                    words.append((buffer['value'], buffer['description']))
                    buffer['value'] = char
                    buffer['description'] = 'OPERATOR'
                elif type == 'RIGHT_BR':
                    state = 'SPACE'
                    words.append((buffer['value'], buffer['description']))
                    buffer['value'] = char
                    buffer['description'] = 'RIGHT_BR'
                elif type == 'SEMICOLON':
                    state = 'SPACE'
                    words.append((buffer['value'], buffer['description']))
                    buffer['value'] = char
                    buffer['description'] = 'SEMICOLON'
                else:
                    state = 'ERROR'
            case 'HEX_CONST':
                if type == 'HEX_LETTER' or type == 'HEX_DIGIT':
                    state = 'HEX_CONST'
                    buffer['value'] += char
                elif type == 'OPERATOR':
                    words.append((buffer['value'], buffer['description']))
                    state = 'SPACE'
                    buffer['value'] = char
                    buffer['description'] = 'OPERATOR'
                elif type == 'SPACE':
                    state = 'SPACE'
                else:
                    state = 'ERROR'
            case 'IDENT':
                if type in ['LETTER', 'HEX_LETTER']:
                    state = 'IDENT'
                    buffer['value'] += char
                elif type == 'DIGIT':
                    state = 'IDENT'
                    buffer['value'] += char
                elif type == 'SPACE':
                    state = 'SPACE'
                elif type == 'OPERATOR':
                    words.append((buffer['value'], buffer['description']))
                    buffer['value'] = char
                    buffer['description'] = 'OPERATOR'
                elif type == 'COMPARATOR':
                    state = 'COMPARATOR'
                    words.append((buffer['value'], buffer['description']))
                    buffer['value'] = char
                    buffer['description'] = 'COMPARATOR'
                elif type == 'RIGHT_BR':
                    state = 'SPACE'
                    words.append((buffer['value'], buffer['description']))
                    buffer['value'] = char
                    buffer['description'] = 'RIGHT_BR'
                elif type == 'LEFT_BR':
                    state = 'SPACE'
                    words.append((buffer['value'], buffer['description']))
                    buffer['value'] = char
                    buffer['description'] = 'LEFT_BR'
                else:
                    state = 'ERROR'
            case 'COMPARATOR':
                if type == 'DIGIT':
                    state = 'INT'
                    words.append((buffer['value'], buffer['description']))
                    buffer['value'] = char
                    buffer['description'] = 'INT'
                elif type == 'SPACE':
                    state = 'SPACE'
                elif type == 'OPERATOR':
                    words.append((buffer['value'], buffer['description']))
                    state = 'SPACE'
                    buffer['value'] = char
                    buffer['description'] = 'OPERATOR'
                elif type == 'COMPARATOR':
                    state = 'COMPARATOR'
                    buffer['value'] += char
                else:
                    state = 'ERROR'
    words.append((buffer['value'], buffer['description']))
    words.pop(0)
    return words
