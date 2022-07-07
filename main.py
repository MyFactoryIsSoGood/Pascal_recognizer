import read_write as file_manager
import my_transliter
import my_lexer
import keywords
import my_syntax

data = file_manager.read_data()
lexemes = my_transliter.transliterate(data)
# print(lexemes)
if not lexemes:
    file_manager.write_data(False)
    # print('REJECTED 1')

words = my_lexer.Lexer(lexemes)
if not words:
    file_manager.write_data(False)
    # print('REJECTED 2')

# chain = file_manager.read_data()
#
# transliterated = tlr.Transliterator(chain)
# # Lexem(symbol='A', cls='letter')
# # Lexem(symbol=':', cls='col')
#
# words = lexer.Lexer(transliterated)
# # Lexem(symbol='myvar', cls='ident')
# # Lexem(symbol=':', cls='col')
#
if keywords.Keywords(words):
    file_manager.write_data(False)
    # print('REJECTED 3')
else:
    if my_syntax.Syntax(words):
        file_manager.write_data(True)
        print('ACCEPTED')
    else:
        file_manager.write_data(False)
        # print('REJECTED 4')
#
#
# result = syntax.Syntax(words)
#
# file_manager.write_data(result)
