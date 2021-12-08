import numpy as np
from math import inf

# board = [[' ', ' ', ' '],
#        [' ', ' ', ' '],
#       [' ', ' ', ' ']]

human = 'X'
bot = 'O'


def checkForDraw(game):
    draw = True
    for i in range(3):
        for j in range(3):
            if game[i][j] is ' ':
                draw = False
    return draw


def checkForWin(game):
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
    return [False, False]


def insertLetter(b, player, row, column):
    if row not in range(3) or column not in range(3):
        print("Enter a valid space.\n")
        r = int(input("Enter row (0-2): "))
        c = int(input("Enter column (0-2): "))
        insertLetter(b, human, r, c)
        return
    if b[row][column] is not ' ':
        print("Space is not empty.\n")
        r = int(input("Enter row (0-2): "))
        c = int(input("Enter column (0-2): "))
        insertLetter(b, human, r, c)
        return

    if player == human:
        b[row][column] = human
    elif player == bot:
        b[row][column] = bot
    return


def computeBestMove(b):
    bestScore = -np.Inf
    bestMove = [-1, -1]

    for i in range(3):
        for j in range(3):
            if b[i][j] == ' ':
                b[i][j] = bot
                score = minimax(b, False)
                b[i][j] = ' '
                if (score > bestScore):
                    bestScore = score
                    bestMove = [i, j]
    insertLetter(b, bot, bestMove[0], bestMove[1])


def minimax(b, isMaximizing):
    if checkForDraw(b):
        return 0
    elif checkForWin(b)[0] == bot:
        return 100
    elif checkForWin(b)[0] == human:
        return -100

    if isMaximizing:
        bestScore = -np.Inf

        for i in range(3):
            for j in range(3):
                if b[i][j] == ' ':
                    b[i][j] = bot
                    score = minimax(b, False)
                    b[i][j] = ' '
                    if (score > bestScore):
                        bestScore = score
        return bestScore

    else:
        bestScore = np.inf
        for i in range(3):
            for j in range(3):
                if b[i][j] == ' ':
                    b[i][j] = human
                    score = minimax(b, True)
                    b[i][j] = ' '
                    if (score < bestScore):
                        bestScore = score
        return bestScore


def print_board(game):
    print('-------------')
    print('| ' + str(game[0][0]) + ' | ' + str(game[0][1]) + ' | ' + str(game[0][2]) + ' |')
    print('-------------')
    print('| ' + str(game[1][0]) + ' | ' + str(game[1][1]) + ' | ' + str(game[1][2]) + ' |')
    print('-------------')
    print('| ' + str(game[2][0]) + ' | ' + str(game[2][1]) + ' | ' + str(game[2][2]) + ' |')
    print('-------------')


def main():
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    while checkForWin(board)[1] is not "Win":
        computeBestMove(board)
        print_board(board)
        if checkForWin(board)[1] is "Win": break
        row = int(input("Enter a row (0-2): "))
        column = int(input("Enter a column (0-2): "))
        insertLetter(board, human, row, column)
        print_board(board)

    if checkForWin(board)[0] == human:
        print("Impossible! The human wins! \n")
    elif checkForWin(board)[0] == bot:
        print("The bot wins again! \n")
    elif checkForDraw(board):
        print("Draw!")

    again = input("Play again? (y/n): ")
    if again == 'y' or again == "Y":
        print("Please wait a second...\n")
        main()
        return
    else:
        quit()


if __name__ == '__main__':
    main()
