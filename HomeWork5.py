# # Задача 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв""

# txt = input("Введите слова через пробел:\n")
# find_txt = "абв"
# lst = [i for i in txt.split() if find_txt not in i]
# print(f'Вот, полюбутесь: {" ".join(lst)}')



# Задача 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# from random import *
# import os


# message = ['ходи быстрее', 'так до утра сидеть будем', 'да не стесняйся', 'давай давай',
#            'долго думаешь']

# from random import randint


# def player_vs_bot():
#     candies_total = 2021
#     max_take = 28
#     player_1 = input('\nНапишите свое имя: ')
#     player_2 = 'Адская вычислительная машина'
#     players = [player_1, player_2]
#     print(f'\nСегодня {player_1} и  {player_2} будут выяснять отношения!\n')
#     print('\nКинем виртуальный жребий\n')

#     lucky = randint(-1, 0)

#     print(f'Первым ходит {players[lucky+1]}')

#     while candies_total > 0:
#         lucky += 1

#         if players[lucky % 2] == 'Компьютер':
#             print(
#                 f'\nХодит {players[lucky%2]} \nОсталось конфет {candies_total}. \n{choice(message)}: ')

#             if candies_total < 29:
#                 step = candies_total
#             else:
#                 delenie = candies_total//28
#                 step = candies_total - ((delenie*max_take)+1)
#                 if step == -1:
#                     step = max_take -1
#                 if step == 0:
#                     step = max_take
#             while step > 28 or step < 1:
#                 step = randint(1,28)
#             print(step)
#         else:
#             step = int(input(f'\nХодит  {players[lucky%2]} \nКонфет осталось {candies_total} {choice(message)}:  '))
#             while step > max_take or step > candies_total:
#                 step = int(input(f'\nПомни, не больше {max_take} конфет ты можешь забрать за раз '))
#         candies_total = candies_total - step

#     print(f'Конфет осталось {candies_total} \nПобедил {players[lucky%2]}')

# player_vs_bot()



# Задача 3. Создайте программу для игры в ""Крестики-нолики""


board = list(range(1,10)) # задаем сетку

def draw_board(board):    # рисуем доску для игры
    print ("-" * 13)
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print ("-" * 13)

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print ("Введите число которе не занято на доске")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print ("Занято")
        else:
            print ("Введите число из доступных")

def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print (tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    draw_board(board)

main(board)