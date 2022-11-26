import requests
import random
import json
from classes import BasicWord

WORDS_DATA_SOURCE_URL = 'https://www.jsonkeeper.com/b/3ORL'


def load_random_word():
    """
    Функция для загрузки с внешнего ресурса списка: Главное слово, составные слова.
    Возвращает список
    """

    get_words_json = requests.get(WORDS_DATA_SOURCE_URL)
    get_words = json.loads(get_words_json.text)
    random_word = random.choice(get_words)

    original_word = random_word['word']
    subwords = random_word['subwords']

    basic_word = BasicWord(original_word, subwords)
    return basic_word
