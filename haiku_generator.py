from text_processor import pipe
from poet import compose


def main():
    corpus = pipe.ReadAndClean('corpus.txt')
    corpus.process_text()
    poet = compose.Poet(corpus.processed_text)
    try:
        poet.real_poetry_generator()
    except:
        print('Поэт пьян: перезапустите генератор.')
        return


if __name__ == '__main__':
    main()
