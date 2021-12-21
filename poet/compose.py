import random

from syllables_counter import syllables_counter
    
    def pick_the_word(self):
        """Выбираем случайное слово и считаем число слогов."""
        first_word = random.choise(self.corpus)
        num_syls = syllables_counter.syllables_counter(first_word)
        if num_syls > 4:
            self.pick_the_word(self.corpus)
        else:
            return(first_word, num_syls)