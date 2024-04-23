'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.

------------------------------------------------------------------

Solution Description: 
My initial idea would be to iterate through the board one element at a time, and assign
a list with all the possible final values of the element taking into account the
contents of the row, column, and block that element occupies. Once every empty 
element is assigned a list of numbers, the program will iterate through again and
if there are any elements with a single potential value, assign that value to the element.
The thinking is that as this happens and the potential values go down for other
elements, the program will steadily approach a final solution.
'''

from typing import List

board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]


def get_block(row:int,col:int)->List[str]:
    x, y = 3*(row//3),3*(col//3)
    block = []
    for i in range(x, y + 3):
        block.extend(board[i][y:y+3])
        return block

def solveSudoku(board: List[List[str]]) -> None:
        for i in range(len(board)):
            row = board[i]
            for j in range(len(board[i])): 
                poss = range(1,10)
                element = board[i][j]
                column = [x[j] for x in board]
                block = get_block(i,j)


def checkSolved(board: List[List[str]]) -> bool:
    def checkSection(section:List[str])-> bool:
        seen = set()
        for cell in section:
            if cell != '.':
                if cell in seen:
                    return False
                seen.add(cell)
        return True
        
    for i in range(9):
        row = board[i]
        col = [board[j][i] for j in range(9)]
        if not (checkSection(row) and checkSection(col)):
            return False
    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = get_block(i, j)
            if not checkSection(block):
                return False
    return True

if __name__ == '__main__':
    solveSudoku(board)
    print(f'\n Solved={checkSolved(board)}')