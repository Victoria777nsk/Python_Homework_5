'''
a) Добавьте игру против бота
b) * Подумайте как наделить бота ""интеллектом""
'''
from random import getrandbits
from Task_1_Two_people import Current_Situation, Enter_Candies_Quantity

candies = 201
max_candies = 28

player_1 = input('Введите ваше имя: ')
player_2 = 'Компьютер'

print(f'Начинаем игру! Игрок: {player_1}. Ваш соперник: {player_2}.')
print('Давайте решим - кто же первым начнет игру?')

first_move = bool(getrandbits(1))
if first_move == 1:
    print(f'Первый ход делает {player_1}!')
else:
    print(f'Первый ход делает {player_2}!')

count_player_1 = 0      # Счетчик количества конфет у игрока 1.
count_player_2 = 0      # Счетчик количества конфет у игрока 2.

while candies > 28:
    if first_move:
        k = Enter_Candies_Quantity(player_1)          # Игрок вводит количество конфет.
        count_player_1 += k                           # Прибавляем взятые конфеты к счетчику игрока.
        candies -= k                                  # Отнимаем от общего количества конфет уже взятые.
        first_move = False                            # Переход хода к боту.
        Current_Situation(player_1, k, count_player_1, candies)
    else:
        k = candies % 29                              # Компьютер забирает остаток от целочисленного деления имеющегося..
        count_player_2 += k                           # количества конфет на количество, которое можно взять за 1 ход + 1.
        candies -= k                                  # Отнимаем от общего количества конфет уже взятые.
        first_move = True                             # Переход хода к игроку 1.
        print('Я сделал ход, теперь ваша очередь!')
        Current_Situation(player_2, k, count_player_2, candies)

if first_move:                                        # Определяем победителя, когда осталось <= 28 конфет.
    print(f'Ура! {player_1}, вы победили!')
else:
    print(f'Увы, компьютер вас обыграл :)')
