from classes import Player
from utils import load_random_word


user_name = input('Введите имя игрока \n')
user = Player(user_name)                               # создаём объект класса Player
basic_word = load_random_word()                        # загружаем данные по URL и создаем объект класса BasicWord

print(f'''Привет, {user_name}!
Составьте {basic_word.number_subwords()} слов из слова {basic_word.original_word.upper()}
Слова должны быть не короче 3 букв
Поехали, ваше первое слово?''')                        # приветствие

for subword in range(basic_word.number_subwords()):    # создаем цикл по количеству подслов
    basic_word.user_word = input()                     # пользователь вводит подслово, присваиваем ввод классу Basicword
    user.user_word = basic_word.user_word              # присваиваем ввод пользователя классу Player

    if basic_word.user_word == 'stop':                 # останавливаем игру при вводе 'stop'
        break

    if user.check_user_word():                         # проверяем использовал ли пользователь уже это слово
        print('Вы уже использовали такое слово, попробуйте ещё раз')
        continue
    elif basic_word.check_subwords():                  # проверяем есть ли слово в списке подслов
        print('Верно!')
        user.word_into_subwords()
    else:
        print('Неверно')                               # если нет, то выводим 'неверно'

print(f'''слова закончились, игра завершена!
вы угадали {user.number_of_words_used()} слов!''')     # Вывод статистики
