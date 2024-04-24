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

Final Solution:
After looking into backtracing algorithms, I implemented one using a nested 'for' loop
and function recursion. The program will try using a value out of the possible values
for that cell, then it will call the function again to see if there is a valid solution
past that. If there is, it will return True, the value will be saved, and it will move to
the next cell. If it returns false due to a solution not existing, it will reset the 
cell and try again until it gets the right value. This is repeated for every empty cell
until a solution is reached.
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

def possible(board, row, col, num):
    if board[row][col] != '.':
        return False
    if str(num) in board[row]:
        return False
    for i in range(9):
        if board[i][col] == str(num):
            return False
    block_row,block_col = 3*(row//3),3*(col//3)
    for x in range(block_row,block_row+3):
        for z in range(block_col,block_col+3):
            if board[x][z] == str(num):
                return False
    return True

def checkSolved(board: List[list]) -> bool:
    def get_block(row:int,col:int)->List[str]:
        x, y = 3*(row//3),3*(col//3)
        block = []
        for z in board[y:y+3]:
            block.extend(z[x:x+3])
        return block
    
    def checkSection(section:list)->bool:
        seen = set()
        for cell in section:
            if cell != '.':
                if cell in seen:
                    return False
                seen.add(cell)
            else: pass
        return True
        
    for i in range(9):
        row = board[i]
        col = [board[j][i] for j in range(9)]
        if not (checkSection(row) and checkSection(col)):
            return False
    
    for row in range(3):
        for col in range(3):
            block = get_block(row*3,col*3)
            if not checkSection(block):
                print(block)
                return False
    return True

def solveSudoku(board: List[List[str]]) -> None:
    for row in range(9):
        for col in range(9):
            if board[row][col] == '.':
                for num in range(1,10):
                    if possible(board,row,col,num):
                        board[row][col] = str(num)
                        if solveSudoku(board):
                            return True    
                        board[row][col] = '.'
                return False
    return True

if __name__ == '__main__':
    solveSudoku(board)
    for row in board: print(f'\n {row}')
    print(f'\n Solved: {checkSolved(board)}')