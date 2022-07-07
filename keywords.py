keywords_list = ["and", "array", "asm", "begin", "break", "case", "const", "constructor", "continue", "destructor",
                 "div",
                 "do", "downto", "else", "end", "false", "file", "for", "function", "goto", "if", "implementation",
                 "in",
                 "inline", "interface", "label", "mod", "nil", "not", "object", "of", "on", "operator", "or", "packed",
                 "procedure", "program", "record", "repeat", "set", "shl", "shr", "string", "then", "to", "true",
                 "type",
                 "unit", "until", "uses", "var", "while", "with", "xor"]


def Keywords(words):
    for i in range(len(words)):
        if words [i][1] == "identifier":
            if words[i][0].lower() not in keywords_list:
                continue
            else:
                return True
    return False
