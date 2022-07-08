keywords_list = ["and", "array", "asm", "begin", "break", "case", "const", "constructor", "continue", "destructor",
                 "div",
                 "do", "downto", "else", "end", "false", "file", "for", "function", "goto", "if", "implementation",
                 "in",
                 "inline", "interface", "label", "mod", "nil", "not", "object", "of", "on", "operator", "or", "packed",
                 "procedure", "program", "record", "repeat", "set", "shl", "shr", "string", "then", "to", "true",
                 "type",
                 "unit", "until", "uses", "var", "while", "with", "xor"]


def keywords(words: list) -> list:
    buffer = []
    for i,word in enumerate(words):
        if word[1] == "IDENT":
            if word[0].lower() in keywords_list:
                buffer.append((word[0], 'KEY_' + word[0].upper()))
                continue
        buffer.append(words[i])
    return buffer
