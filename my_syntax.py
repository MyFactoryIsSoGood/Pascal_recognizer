allowed = [
    'REPEAT identifier open_bracket const_sign operator identifier close_bracket UNTIL identifier comparator integer semicolon',
    'REPEAT identifier open_bracket const_sign operator digit close_bracket UNTIL identifier comparator integer semicolon',
]


def Syntax(words):
    chain = ' '.join([i [1] for i in words])
    if chain in allowed:
        operators = [i for i in words if i [1] == 'operator']
        comparator = [i for i in words if i [1] == 'comparator'][0][0]
        if comparator not in ['>', '<', '>=', '<=', '<>']:
            return False
        if len(operators) <= 2 or operators [1] [0] == '-':
            return True
        else:
            return False
