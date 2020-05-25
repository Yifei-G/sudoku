from board import displayBoard
from check import isNumUnique, isBoardComplete
checkList = []
editableList = []


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

        # Check if user is trying to modify a pre-defined number or not.
        # We only want user to modify empty grid (which the initial value is always "_")
        # After the empty grid has been modified,
        # we put its position to the editable list, in case user needs to
        # modify the value in the future.
        if (board[rowNum][columnNum] != "_") and (userPosition not in editableList):
            print("You can't modify pre-defined numbers!")
        else:
            # TODO: correct the following verfication logic
            if not isBoardComplete(board):
                    # the board is not complete
                if isNumUnique(board, userPosition, userData):
                    checkList.append("CorrectMove")
                else:
                    checkList.append("IncorrectMove")
            else:
                    # the board is completed but with error
                if isNumUnique(board, userPosition, userData):
                    # remove 1 IncorrectMove from the check list
                    checkList.remove("IncorrectMove")
                    checkList.append("CorrectMove")
                else:
                    # in case user has made more errors, add 1
                    # IncorrectMove
                    checkList.append("IncorrectMove")
                    checkList.remove("CorrectMove")
            # add this position to the editable list
            if userPosition not in editableList:
                editableList.append(userPosition)

            board[rowNum][columnNum] = userData
            return checkList

    except ValueError:
        print("You have entered an invalid row or column number. Please enter only NUMBER between 1-9\n")
        userInput(board)
    except AssertionError:
        print("You have entered an invalid number, please only enter only NUMBER between 1-9\n")
        userInput(board)
