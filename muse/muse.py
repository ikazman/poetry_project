from collections import defaultdict

from syllables_counter import syllables_counter

class Muse:
    """Цепь Маркова."""

    def __init__(self, corpus):
        self.corpus = corpus
        self.length = len(corpus)
        self.dict_word_to_word = defaultdict(list)
        self.dict_word_to_two_word = defaultdict(list)

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
                key = ' '.join(word, self.corpus[idx + 1])
                suffix = self.corpus[idx + 2]
                self.dict_word_to_two_word[key].append(suffix)

    def word_after_single(self, prefix, suffix_map, current_syls, target_syls):
        """Возвращаем все допустимые варианты после первого слова из копуса."""
        accepted_words = []
        suffixes = suffix_map.get(prefix)
        if suffixes:
            for candidate in suffixes:
                num_syls = syllables_counter.syllables_counter(candidate)
                if current_syls + num_syls < target_syls:
                    accepted_words.append(candidate)
        return accepted_words

    def word_after_double(self, prefix, suffix_map, current_syls, target_syls):
        """Возвращаем все допустимые варианты после пары слов из копуса."""
        accepted_words = []
        suffixes = suffix_map.get(prefix)
        if suffixes:
            for candidate in suffixes:
                num_syls = syllables_counter.syllables_counter(candidate)
                if current_syls + num_syls < target_syls:
                    accepted_words.append(candidate)
        return accepted_words


