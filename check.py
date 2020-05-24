from random import randrange
uniqueNum = False
taileLevel = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]


# A function to check if the board is full
def checkBoard(board):
    for row in range(0, 9):
        for column in range(0, 9):
            if board[row][column] == "_":
                return False
    return True


def createRandomPosition():
    j = 0
    randomPosition = ()
    while j < 2:
        randomPosition += (randrange(0, 9),)
        j += 1
    return randomPosition


def copyBoard(board):
    tempRow = 0
    tempColumn = 0
    tempBoard = []
    while tempRow < 9:
        tempBoard.append([])
        while tempColumn < 9:
            tempBoard[tempRow].append(board[tempRow][tempColumn])
            tempColumn += 1
        tempRow += 1
        tempColumn = 0
    return tempBoard


# Generate a list of value's row
def createRowList(board, row):
    myList = board[row]
    return myList


# Generate a list of value's column
def createColumnList(board, column):
    myList = []
    for index in range(len(board)):
        columnValue = board[index][column]
        myList.append(columnValue)
    return myList


# use the value position to determine which is the initial position of value's Taile
# posible values are: (0,0) (0,3) (0,6) (3,0) (3,3) (3,6) (6,0) (6,3) (6,6)
def createTailePosition(position):
    if position in taileLevel[0]:
        position = 0
        return position
    elif position in taileLevel[1]:
        position = 3
        return position
    elif position in taileLevel[2]:
        position = 6
        return position


# Generate a list of value's taile
def createTaileList(board, row, column):
    myList = []
    initTaileRow = createTailePosition(row)
    columnIndex = createTailePosition(column)
    initTaileColumn = columnIndex

    endTaileRow = initTaileRow + 2
    endTaileColumn = columnIndex + 2

    while initTaileRow <= endTaileRow:
        while columnIndex <= endTaileColumn:
            taileValue = board[initTaileRow][columnIndex]
            myList.append(taileValue)
            columnIndex += 1
        columnIndex = initTaileColumn
        initTaileRow += 1
    return myList


# Check if a value is unique in the board
def isNumUnique(board, position, num):
    row = position[0]
    column = position[1]
    rowList = createRowList(board, row)
    # Check if the number is repeated in row
    if str(num) in rowList:
        uniqueNum = False
        return uniqueNum
    else:
        # Check if the number is repeated in column
        columnList = createColumnList(board, column)
        if str(num) in columnList:
            uniqueNum = False
            return uniqueNum
        else:
            # Check if the number is repeated in taile
            taileList = createTaileList(board, row, column)
            if str(num) in taileList:
                uniqueNum = False
                return uniqueNum
            else:
                uniqueNum = True
                return uniqueNum
