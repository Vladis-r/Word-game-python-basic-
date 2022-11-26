class BasicWord:
    """
    Класс ключевого слова.
    Поля: ключевое слово, набор допустимых подслов
    """
    def __init__(self, original_word, subwords):
        self.original_word = original_word
        self.subwords = subwords
        self.user_word = None

    def __repr__(self):
        """
        :return: ключевое слово, список подслов, ввод пользователя
        """
        return f'{self.original_word} {self.subwords} {self.user_word}'

    def check_subwords(self):
        if self.user_word in self.subwords:
            return True
        return False

    def number_subwords(self):
        return len(self.subwords)


class Player:
    """
    Класс пользователя
    Поля: имя пользователя
    """
    def __init__(self, user_name):
        self.user_name = user_name
        self.used_subwords = []
        self.user_word = None

    def __repr__(self):
        """
        :return: имя пользователя, использованные слова, слово пользователя
        """
        return f'{self.user_name} {self.used_subwords} {self.user_word}'

    def number_of_words_used(self):
        """
        :return: количество использованных слов
        """
        return len(self.used_subwords)

    def word_into_subwords(self):
        """
        Метод добавляет слово пользователя в список использованных слов
        """
        self.used_subwords.append(self.user_word)

    def check_user_word(self):
        """
        :return: булевое значение, если слово пользователя в списке использованных слов
        """
        return self.user_word in self.used_subwords
