import read_write as file_manager
import transliterator
import lexical
import keywords
import syntax

if __name__ == '__main__':
    data = file_manager.read_data()
    lexemes = transliterator.transliterate(data)

    words = lexical.lex(lexemes)

    words = keywords.keywords(words)
    for i in words:
        print(i, end=', ')
    accepted = syntax.syntax(words)
    file_manager.write_data(accepted)
