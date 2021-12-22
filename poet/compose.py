import random
from collections import defaultdict

from syllables_counter import syllables_counter


class Poet:
    """Класс для генерации строк."""

    def __init__(self, corpus):
        self.corpus = corpus
        self.length = len(corpus)
        self.dict_word_to_word = defaultdict(list)
        self.dict_word_to_two_word = defaultdict(list)
        self.poem = None

    def map_word_to_word(self):
        """Размечиваем второе слово после первого."""
        limit = self.length - 1
        for idx, word in enumerate(self.corpus):
            if idx < limit:
                suffix = self.corpus[idx + 1]
                self.dict_word_to_word[word].append(suffix)

    def map_word_to_two_words(self):
        """Размечиваем третье слово после первых двух."""
        limit = self.length - 2
        for idx, word in enumerate(self.corpus):
            if idx < limit:
                key = ' '.join([word, self.corpus[idx + 1]])
                suffix = self.corpus[idx + 2]
                self.dict_word_to_two_word[key].append(suffix)

    def word_after(self, prefix, current_syls, target_syls, cnt='double'):
        """Возвращаем все допустимые варианты слова из копуса."""
        accepted_words = []
        if cnt == 'single':
            suffixes = self.dict_word_to_word.get(prefix)
        else:
            suffixes = self.dict_word_to_two_word.get(prefix)

        if suffixes:
            for candidate in suffixes:
                num_syls = syllables_counter.syllables_counter(candidate)
                if current_syls + num_syls <= target_syls:
                    accepted_words.append(candidate)
        return accepted_words

    def pick_the_word(self):
        """Выбираем случайное слово и считаем число слогов."""
        first_word = random.choice(self.corpus)
        num_syls = syllables_counter.syllables_counter(first_word)
        if num_syls > 4:
            self.pick_the_word()
        else:
            return(first_word, num_syls)

    def haiuku_line(self, end_prev_line, target_syls):
        """Генерируем строку для хайку."""
        line = '2/3'
        line_syls = 0
        current_line = []

        if len(end_prev_line) == 0:
            line = '1'
            word, num_syls = self.pick_the_word()
            current_line.append(word)
            line_syls += num_syls
            word_choices = self.word_after(word,
                                           line_syls,
                                           target_syls,
                                           'single')
            while len(word_choices) == 0:
                prefix = random.choice(self.corpus)
                word_choices = self.word_after(prefix,
                                               line_syls,
                                               target_syls,
                                               'single')
            word = random.choice(word_choices)
            num_syls = syllables_counter.syllables_counter(word)
            line_syls += num_syls
            current_line.append(word)
            if line_syls == target_syls:
                end_prev_line.extend(current_line[-2:])
                return current_line, end_prev_line
        else:
            current_line.extend(end_prev_line)

        while True:
            prefix = ' '.join([current_line[-2], current_line[-1]])
            word_choices = self.word_after(prefix,
                                           line_syls,
                                           target_syls)
            while len(word_choices) == 0:
                idx = random.randint(0, self.length - 2)
                prefix = ' '.join([self.corpus[idx], self.corpus[idx + 1]])
                word_choices = self.word_after(prefix,
                                               line_syls,
                                               target_syls)
            word = random.choice(word_choices)
            num_syls = syllables_counter.syllables_counter(word)

            if line_syls + num_syls > target_syls:
                continue
            elif line_syls + num_syls < target_syls:
                current_line.append(word)
                line_syls += num_syls
            elif line_syls + num_syls == target_syls:
                current_line.append(word)
                break

        end_prev_line = []
        end_prev_line.extend(current_line[-2:])

        if line == '1':
            final_line = current_line[:]
        else:
            final_line = current_line[2:]

        return final_line, end_prev_line

    def real_poetry_generator(self):
        """Генерируем весь стих."""
        self.poem = []
        end_prev_line = []
        self.map_word_to_word()
        self.map_word_to_two_words()
        first_line, end_prev_line_first = self.haiuku_line(end_prev_line, 5)
        self.poem.append(first_line)
        line, end_prev_line_second = self.haiuku_line(end_prev_line_first, 7)
        self.poem.append(line)
        line, _ = self.haiuku_line(end_prev_line_second, 5)
        self.poem.append(line)

        for line in self.poem:
            print(' '.join(line))
