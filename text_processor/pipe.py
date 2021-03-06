class ReadAndClean:
    """Класс для чтения и очищения корпуса."""

    def __init__(self, file):
        self.path = 'data/'
        self.text = None
        self.processed_text = None
        self.file_name = file

    def read_corpus(self):
        """Открываем файл с тренировочным текстом."""
        corpus_path = self.path + self.file_name
        with open(corpus_path, 'r', encoding='utf-8') as input_file:
            self.text = input_file.read()

    def clean_text(self):
        """Очищаем текст от знаков препинаний, приводим к одному регистру."""
        punctuation = '«»"'
        text_without_punct = ''.join(
            [char for char in self.text if char not in punctuation])

        self.processed_text = [word.lower() for word
                               in text_without_punct.split()]

    def process_text(self):
        """Функция для запуска пайплайна."""
        self.read_corpus()
        self.clean_text()
