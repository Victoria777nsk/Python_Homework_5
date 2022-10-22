'''
Задача 2. Создайте программу для игры в "Крестики-нолики".
'''
from random import getrandbits

game_board = [1,2,3,      # Создаем игровое поле размерностью 3 х 3.
              4,5,6,
              7,8,9]
 
victories = [[0,1,2],     # Определяем победные линии из "Х" или "0" в игре.
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]
 
def Print_Game_Board():                # Метод вывода игрового поля на экран
    print(game_board[0], end = " ")
    print(game_board[1], end = " ")
    print(game_board[2])
 
    print(game_board[3], end = " ")
    print(game_board[4], end = " ")
    print(game_board[5])
 
    print(game_board[6], end = " ")
    print(game_board[7], end = " ")
    print(game_board[8])    
    
def Step_Game_Board(step,symbol):      # Метод хода в ячейку
    ind = game_board.index(step)       # index() возвращает индекс указанного элемента (step) в списке (на игровом поле)
    game_board[ind] = symbol
 
def Current_Situation():               # Вывод текущего результата игры
    win = ""
    for i in victories:
        if game_board[i[0]] == "X" and game_board[i[1]] == "X" and game_board[i[2]] == "X":
            win = "X"
        if game_board[i[0]] == "O" and game_board[i[1]] == "O" and game_board[i[2]] == "O":
            win = "O"   
    return win
 
# Основная программа:

player_1 = input('Введите имя первого игрока: ')
player_2 = input('Введите имя второго игрока: ')

first_move = bool(getrandbits(1))   # Определяем, кто из игроков будет ходить первым 
if first_move == True:              # (с помощью генерации случайного логического значения).
    print(f'Первый ход делает {player_1}!')
else:
    print(f'Первый ход делает {player_2}!')

game_over = False
counter = 0                   # Вводим счетчик ходов.

while game_over == False:     # Пока игра не будет окончена.
    Print_Game_Board()        # Выводим игровое поле на экран.
    if first_move == True:    # Спрашиваем у игрока, куда делать ход.
        symbol = "X"          # По умолчанию 1-ый игрок играет "X".
        step = int(input(f'{player_1}, ваш ход: '))
        counter += 1
        first_move = False    # переход хода к игроку 2.
    else:
        symbol = "O"          # По умолчанию 2-ой игрок играет "О".
        step = int(input(f'{player_2}, ваш ход: '))
        counter += 1
        first_move = True     # Переход хода к игроку 1.
    Step_Game_Board(step,symbol) # Делаем ход в указанную ячейку
    win = Current_Situation()    # Определяем победителя
    if win != "" or counter == 9:
        game_over = True
    else:
        game_over = False 

Print_Game_Board()       # Игра окончена. Показываем игровое поле и объявляем победителя. 

if win == "X":
    print(f'Победил {win}')
    print(f'{player_1}, поздравляем с победой!')
elif win == "O":
    print(f'Победил {win}')
    print(f'{player_2}, поздравляем с победой!')
else:
    print('Игра окончена! У вас ничья!')