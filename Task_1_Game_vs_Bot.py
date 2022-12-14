'''
a) Добавьте игру против бота
b) * Подумайте как наделить бота ""интеллектом""
'''
from random import getrandbits

candies = 201
max_candies = 28

player_1 = input('Введите ваше имя: ')
player_2 = 'Компьютер'

print(f'Начинаем игру! Игрок: {player_1}. Ваш соперник: {player_2}.')
print('\nДавайте решим - кто же первым начнет игру?\n')

first_move = True
print(f'Первый ход делает {player_2}!')   # Первый ход автоматически делает компьютер, пытаясь реализовать стратегию для победы.

def Enter_Candies_Quantity(name):        # Запрашиваем у игрока ввод количества конфет.
    k = int(input(f'{name}, какое количество конфет возьмете (от 1 до 28): '))
    while k < 1 or k > 28:
        k = int(input(f'Ошибка! {name}, введите количество от 1 до 28: '))
    return k

def Current_Situation(candies):           # Выводим на экран текущую ситуацию (сколько конфет осталось на столе).
    print(f'На столе осталось: {candies} конфет(-ы).')

while candies > 28:
    if first_move == True:
        k = candies % 29                              # Компьютер забирает остаток от целочисленного деления имеющегося 
                                                      # количества конфет на количество, которое можно взять за 1 ход + 1.
        candies -= k                                  # Отнимаем от общего количества конфет уже взятые.
        print(f'\nЯ сделал свой ход и взял {k} конфет(-ы).\n')
        Current_Situation(candies)
        first_move = False                            # Переход хода к игроку 1.
    else:
        k = Enter_Candies_Quantity(player_1)          # Игрок вводит количество конфет.
        candies -= k                                  # Отнимаем от общего количества конфет уже взятые.
        first_move = True                             # Переход хода к боту.
        Current_Situation(candies)

if first_move:                                        # Определяем победителя, когда осталось <= 28 конфет.
    print(f'Увы, компьютер вас обыграл.')
else:
    print(f'Ура! {player_1}, вы победили!')