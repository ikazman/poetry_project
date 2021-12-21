from text_processor import pipe
from poet import compose


def main():
    final = []
    end_prev_line = []
    corpus = pipe.ReadAndClean('corpus.txt')
    corpus.process_text()
    poet = compose.Poet(corpus.processed_text)
    poet.map_word_to_word()
    poet.map_word_to_two_words()
    first_line, end_prev_line_first = poet.haiuku_line(end_prev_line, 5)
    final.append(first_line)
    line, end_prev_line_second = poet.haiuku_line(end_prev_line_first, 7)
    final.append(line)
    line, _ = poet.haiuku_line(end_prev_line_second, 5)
    final.append(line)

    for line in final:
        print(' '.join(line))


if __name__ == '__main__':
    main()
