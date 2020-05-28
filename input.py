from board import displayBoard
from check import isNumUnique, isBoardComplete
userSolution = {}
editableList = []
isSudoku = False


def userInput(board, solution):
    try:
        global isSudoku
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

        # Check if user is trying to modify a pre-defined number or not.
        # We only want user to modify empty grid (which the initial value is always "_")
        # After the empty grid has been modified,
        # we put its position to the editable list, in case user needs to
        # modify the value in the future.
        if (board[rowNum][columnNum] != "_") and (userPosition not in editableList):
            print("You can't modify pre-defined numbers!")
        else:
            # add this position to the editable list
            if userPosition not in editableList:
                editableList.append(userPosition)
            # add user's number into the user solution dict
            userSolution[userPosition] = userData

            board[rowNum][columnNum] = userData

            # if the boad is completed, compare user's solution with the actual solution. If both dicts are the same
            # The board is Sudoku
            if isBoardComplete(board):
                if userSolution == solution:
                    isSudoku = True

            return isSudoku

    except ValueError:
        print("You have entered an invalid row or column number. Please enter only NUMBER between 1-9\n")
        userInput(board, solution)
    except AssertionError:
        print("You have entered an invalid number, please only enter only NUMBER between 1-9\n")
        userInput(board, solution)
