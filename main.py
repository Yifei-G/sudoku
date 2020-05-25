from check import (createRowList, createColumnList,
                   createTaileList, isBoardComplete,
                   isNumUnique, copyBoard, createRandomPosition)
from board import displayBoard
from input import userInput
from random import randrange

Board = []
Board = [["_" for i in range(9)] for j in range(9)]
loading = "Loading.."


def createRandomBoard(board):
    i = 0
    while i < 30:
        randomPosition = createRandomPosition()
        randomValue = randrange(1, 10)
        if isNumUnique(board, randomPosition, randomValue):
            # if the number is unique in its row,column and taile, then put
            # it into the board
            board[randomPosition[0]][randomPosition[1]] = str(randomValue)
            # increse the i and reset the tulple to generate a new random
            # position
            i += 1


def solveSudoku(board):
    for i in range(0, 81):
        row = i // 9
        column = i % 9
        if board[row][column] == "_":
            for value in range(1, 10):
                position = (row, column)
                if isNumUnique(board, position, value):
                    board[row][column] = str(value)
                    if isBoardComplete(board):
                        return True
                    else:
                        if solveSudoku(board):
                            return True
            break
    board[row][column] = "_"


def removePositions(board):
    i = 0
    tempBoard = []

    while i < 3:
        randomPosition = createRandomPosition()
        randomRow = randomPosition[0]
        randomColumn = randomPosition[1]
        if board[randomRow][randomColumn] != "_":
            origialValue = board[randomRow][randomColumn]
            tempBoard = copyBoard(board)
            tempBoard[randomRow][randomColumn] = "_"
            if solveSudoku(tempBoard):
                board[randomRow][randomColumn] = "_"
                i += 1
            else:
                print("The value can't be extacted!")
                board[randomRow][randomColumn] = origialValue
    displayBoard(tempBoard)


def init():
    global Board, loading
    gameOver = False

    createRandomBoard(Board)
    loading += "."
    print(loading)

    if solveSudoku(Board):
        print("Game loaded!")
        removePositions(Board)

        while not (isBoardComplete(Board) and gameOver):
            displayBoard(Board)
            result = userInput(Board)

            if isBoardComplete(Board):
                if not result:
                    continue
                elif "IncorrectMove" in result:
                    print(
                        "Opss.. Something is not correct! Check it again and make your board Sodoku!!")
                else:
                    gameOver = True
                    break
    else:
        loading += "."
        print(loading)
        Board = [["_" for i in range(9)] for j in range(9)]
        init()


init()

print()
seperateLine = "=" * 55
print(seperateLine)
print("Congrats! This is a Sodoku!!")
displayBoard(Board)
print("Thanks for playing!!!")
