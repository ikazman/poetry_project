VOWELS = 'АЕЁИОУЫЭЮЯаеёиоуыэюя'

def syllables_counter(phrase):
    """Считаем число слогов в слове."""
    num_of_syllas = 0
    phrase = phrase.casefold().strip().split()

    for word in phrase:
        for char in word:
            if char in VOWELS:
                num_of_syllas += 1
    return num_of_syllas     

def main():
    phrase_one = 'Я - Гайбраш Трипвуд, могущественный пират!'
    phrase_two = 'Арррррргх!'
    print('Считаем. Число слогов:')
    print(f'- во фразе "{phrase_one}" - {syllables_counter(phrase_one)}')
    print(f'- во фразе "{phrase_two}" - {syllables_counter(phrase_two)}')

if __name__ == '__main__':
    main()