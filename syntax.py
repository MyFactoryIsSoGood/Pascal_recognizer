def syntax(words: list) -> bool:
    state = 'REPEAT'
    for word in words:
        (value, type) = word
        match state:
            case 'REPEAT':
                if type == 'KEY_REPEAT':
                    state = 'IDENT'
                else:
                    print(False)
                    return False
            case 'IDENT':
                if type == 'IDENT':
                    state = 'OPEN'
                else:
                    return False
            case 'OPEN':
                if type == 'LEFT_BR':
                    state = 'CONST'
                else:
                    return False
            case 'CONST':
                if type == 'HEX_CONST':
                    state = 'OPERATOR'
                else:
                    return False
            case 'OPERATOR':
                if type in ['OPERATOR', 'KEY_DIV', 'KEY_MOD']:
                    state = 'IDENT2'
                else:
                    return False
            case 'IDENT2':
                if type == 'IDENT':
                    state = 'CLOSE'
                else:
                    return False
            case 'CLOSE':
                if type == 'RIGHT_BR':
                    state = 'UNTIL'
                else:
                    return False
            case 'UNTIL':
                if type == 'KEY_UNTIL':
                    state = 'IDENT3'
                else:
                    return False
            case 'IDENT3':
                if type == 'IDENT':
                    state = 'COMPARATOR'
                else:
                    return False
            case 'COMPARATOR':
                if type == 'COMPARATOR':
                    state = 'SIGN'
                else:
                    return False
            case 'SIGN':
                if type == 'OPERATOR' and value in ['-', '+']:
                    state = 'INT'
                elif type == 'INT':
                    state = 'INT'
                else:
                    return False
            case 'INT':
                if type in ['SEMICOLON', 'INT']:
                    state = 'INT'
                else:
                    return False
    return True
