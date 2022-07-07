def Lexer(symbols: list) -> list:
    words = []
    now = [' ', 'None']
    state = "space"

    for s in symbols:
        if s [1] == "letter":  # встречаем Буквы
            if state == "space":
                if now [0] == 'repeat' or now [0] == 'until':
                    words.append((now [0], now [0].upper()))
                else:
                    words.append(tuple(now))
                now [0] = s [0]
                now [1] = "identifier"
                state = "name"
            elif state == 'const':
                if s [0].lower() in ['a', 'b', 'c', 'd', 'e', 'f']:
                    now [0] += s [0]
            elif state == "name":
                now [0] += s [0]
            else:
                # print("letter")
                # print(now)
                # print(words)
                # print(state)
                return []
        elif s [1] == "hex_digit":  # встречаем цифры
            if state == "const":
                now [0] += s [0]
        elif s [1] == "space":  # встречаем Пробел
            state = 'space'
        elif s [1] == "digit":  # встречаем Число
            if state == "name":
                now [0] += s [0]
            elif state == "digit":
                now [0] += s [0]
            elif state == "space":
                if now [0] == 'div' or now [0] == 'mod':
                    words.append((now [0], 'operator'))
                else:
                    words.append(tuple(now))
                now [0] = s [0]
                now [1] = "digit"
                state = "digit"
            elif state == 'comparator':
                words.append(tuple(now))
                now [0] = s [0]
                now [1] = "digit"
                state = "digit"
            elif state == 'const':
                words.append(tuple(now))
                now [0] = s [0]
                now [1] = "digit"
                state = "digit"
        elif s [1] == "semicolon":  # встречаем ;
            if state == "semicolon":
                words.append(tuple(now))
                now [0] = s [0]
                now [1] = "semicolon"
                state = "semicolon"
            elif state == 'space':
                words.append(tuple(now))
                now [0] = s [0]
                now [1] = "semicolon"
                state = "semicolon"
            elif state == 'digit' or state == 'name':
                now[1] = 'integer'
                words.append(tuple(now))
                now [0] = s [0]
                now [1] = "semicolon"
                state = "semicolon"
            else:
                # print("semicol")
                return []
        elif s [1] == "lpar":  # встречаем (
            if state == "name":
                words.append(tuple(now))
                now [0] = s [0]
                now [1] = "open_bracket"
                state = "space"
            elif state == "space":
                words.append(tuple(now))
                now [0] = s [0]
                now [1] = "open_bracket"
                state = "space"
            else:
                # print("(")
                return []
        elif s [1] == "rpar":  # встречаем )
            if state == "digit":
                words.append(tuple(now))
                now [0] = s [0]
                now [1] = "close_bracket"
                state = "space"
            elif state == "space":
                words.append(tuple(now))
                now [0] = s [0]
                now [1] = "close_bracket"
                state = "space"
            else:
                return []
        elif s [1] == 'const_sign':
            words.append(tuple(now))
            now [0] = s [0]
            now [1] = "const_sign"
            state = "const"
        elif s [1] == 'comparator':
            if state == 'comparator':
                now [0] += s [0]
            elif state == 'name':
                words.append(tuple(now))
                now [0] = s [0]
                now [1] = "comparator"
                state = "comparator"
            elif state == 'space':
                words.append(tuple(now))
                now [0] = s [0]
                now [1] = "comparator"
                state = "comparator"
        elif s [1] == 'operator':
            if state == 'comparator':
                words.append(tuple(now))
                now [0] = s [0]
                now [1] = "operator"
                state = "comparator"
            elif state == 'space':
                words.append(tuple(now))
                now [0] = s [0]
                now [1] = "operator"
                state = "name"
            else:
                return []
        else:
            return []

    words.append(tuple(now))
    words.pop(0)
    return words

# chain = file_manager.data_input()
# transliterated = tlr.Transliterator(chain)
# Lexer(transliterated)
# print(Lexer(transliterated))
