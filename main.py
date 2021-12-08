import numpy as np
from math import inf

board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

players = ['X', 'O']


def check_game(game):
    draw = True
    for i in range(3):
        for j in range(3):
            if game[i][j] is ' ':
                draw = False
    if draw is True:
        return None, "Draw"

    # check columns for a win
    if game[0][0] is not ' ' and game[0][0] == game[1][0] == game[2][0]:
        return game[0][0], "Win"
    if game[0][1] is not ' ' and game[0][1] == game[1][1] == game[2][1]:
        return game[0][1], "Win"
    if game[0][2] is not ' ' and game[0][2] == game[1][2] == game[2][2]:
        return game[0][2], "Win"

    # check rows for a win
    if game[0][0] is not ' ' and game[0][0] == game[0][1] == game[0][2]:
        return game[0][0], "Win"
    if game[1][0] is not ' ' and game[1][0] == game[1][1] == game[1][2]:
        return game[1][0], "Win"
    if game[2][0] is not ' ' and game[2][0] == game[2][1] == game[2][2]:
        return game[2][0], "Win"

    # check diagonals for a win
    if game[0][0] is not ' ' and game[0][0] == game[1][1] == game[2][2]:
        return game[0][0], "Win"
    if game[2][0] is not ' ' and game[2][0] == game[1][1] == game[0][2]:
        return game[2][0], "Win"


def minimax(b, player):
    winnerLoser, done = check_game(b)
    if done == "Done" and winnerLoser == 'O':
        return 1
    elif done == "Done" and winnerLoser == 'X':
        return -1
    elif done == "Draw":
        return 0

    moves = []
    empty = []
    for i in range(3):
        for j in range(3):
            if b[i][j] is ' ':
                empty.append((j+1) + i*3) # 2D to 1D mapping
    for cell in empty:
        move = {}
        move['index'] = cell


def print_board(game):
    print('-------------')
    print('| ' + str(game[0][0]) + ' | ' + str(game[0][1]) + ' | ' + str(game[0][2]) + ' |')
    print('-------------')
    print('| ' + str(game[1][0]) + ' | ' + str(game[1][1]) + ' | ' + str(game[1][2]) + ' |')
    print('-------------')
    print('| ' + str(game[2][0]) + ' | ' + str(game[2][1]) + ' | ' + str(game[2][2]) + ' |')
    print('-------------')


if __name__ == '__main__':
    board = [['X', 'O', 'X'],
             ['O', 'O', 'X'],
             ['X', ' ', 'O']]
    print(check_game(board))

