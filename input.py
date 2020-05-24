from board import displayBoard
from check import isNumUnique
checkList = []


def userInput(board):
    try:
        inputRow = int(
            input("Please select between 1-9 the number of the row:"))
        assert (inputRow > 0 and inputRow <= 9)

        inputColumn = int(
            input("Please select between 1-9 the number of the column:"))
        assert (inputColumn > 0 and inputColumn <= 9)

        userData = input("Please enter between 1-9 the number for the game:")
        assert (userData.isdigit()) and (
            int(userData) > 0 and int(userData) <= 9)

        rowNum = inputRow - 1
        columnNum = inputColumn - 1
        userPosition = (rowNum, columnNum)

        if isNumUnique(board, userPosition, userData):
            print("The number is unique")
            checkList.append("CorrectMove")
        else:
            print("The number is not unique")
            checkList.append("IncorrectMove")

        board[rowNum][columnNum] = userData

        return checkList

    except ValueError:
        print("You have entered an invalid row or column number. Please enter only NUMBER between 1-9\n")
        userInput(board)
    except AssertionError:
        print("You have entered an invalid number, please only enter only NUMBER between 1-9\n")
        userInput(board)
