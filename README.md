
## Estimated time
60 minutes

## Level of difficulty
Hard

## Objectives

    improving the student's skills in operating with strings and lists;
    converting strings into lists.

## Scenario

As you probably know, Sudoku is a number-placing puzzle played on a 9x9 board. The player has to fill the board in a very specific way:

    each row of the board must contain all digits from 0 to 9 (the order doesn't matter)
    each column of the board must contain all digits from 0 to 9 (again, the order doesn't matter)
    each of the nine 3x3 "tiles" (we will name them "sub-squares") of the table must contain all digits from 0 to 9.

Your task is to write a program which:

1. Generate a random board with numbers inside in order to help user to solve the board
(Board generation should follow Backtracking algorithm, more details can be found in here:
[Sudoku Algorithm](https://www.101computing.net/sudoku-generator-algorithm/)

2. User can interact with the board by typing the row number (1-9) column number(1-9) and the value(1-9) to fill the empty cell
3. The program reads 9 rows of the Sudoku, each containing 9 digits 
    (check carefully if the data entered are valid, use above criteria for the validation)
4. When Game is finished, print the result whether user has solved the board or not

## Example output:

```
X-----+-----+-----X-----+-----+-----X-----+-----+-----X
|     |     |     |     |     |     |     |     |     |
|  _  |  _  |  8  |  3  |  6  |  _  |  4  |  9  |  7  |
|     |     |     |     |     |     |     |     |     |
X-----+-----+-----X-----+-----+-----X-----+-----+-----X
|     |     |     |     |     |     |     |     |     |
|  _  |  _  |  _  |  5  |  4  |  9  |  2  |  8  |  6  |
|     |     |     |     |     |     |     |     |     |
X-----+-----+-----X-----+-----+-----X-----+-----+-----X
|     |     |     |     |     |     |     |     |     |
|  _  |  4  |  6  |  2  |  _  |  _  |  3  |  5  |  _  |
|     |     |     |     |     |     |     |     |     |
X-----+-----+-----X-----+-----+-----X-----+-----+-----X
|     |     |     |     |     |     |     |     |     |
|  6  |  3  |  9  |  _  |  5  |  _  |  8  |  _  |  _  |
|     |     |     |     |     |     |     |     |     |
X-----+-----+-----X-----+-----+-----X-----+-----+-----X
|     |     |     |     |     |     |     |     |     |
|  _  |  2  |  4  |  _  |  _  |  3  |  7  |  _  |  _  |
|     |     |     |     |     |     |     |     |     |
X-----+-----+-----X-----+-----+-----X-----+-----+-----X
|     |     |     |     |     |     |     |     |     |
|  7  |  1  |  5  |  6  |  _  |  _  |  _  |  4  |  3  |
|     |     |     |     |     |     |     |     |     |
X-----+-----+-----X-----+-----+-----X-----+-----+-----X
|     |     |     |     |     |     |     |     |     |
|  4  |  6  |  _  |  9  |  3  |  _  |  _  |  7  |  8  |
|     |     |     |     |     |     |     |     |     |
X-----+-----+-----X-----+-----+-----X-----+-----+-----X
|     |     |     |     |     |     |     |     |     |
|  5  |  8  |  3  |  4  |  1  |  _  |  6  |  2  |  9  |
|     |     |     |     |     |     |     |     |     |
X-----+-----+-----X-----+-----+-----X-----+-----+-----X
|     |     |     |     |     |     |     |     |     |
|  1  |  9  |  _  |  8  |  2  |  6  |  _  |  _  |  _  |
|     |     |     |     |     |     |     |     |     |
X-----+-----+-----X-----+-----+-----X-----+-----+-----X
```
