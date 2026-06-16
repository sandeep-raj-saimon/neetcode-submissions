from collections import defaultdict
from math import floor
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        matrix = {}
        m = defaultdict(list)
        for i in range(9):
            for j in range(9):
                matrix[tuple([i,j])] = None
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    pass
                else:
                    # checking for violation of sudoku rules
                    for row in range(9):
                        if matrix[tuple([row, j])] == board[i][j]:
                            return False
                    
                    for col in range(9):
                        if matrix[tuple([i, col])] == board[i][j]:
                            return False

                    row = floor(i/3)
                    col = floor(j/3)

                    if board[i][j] in m[tuple([row, col])]:
                        return False
                    matrix[tuple([i,j])] = board[i][j]
                    m[tuple([row, col])].append(board[i][j])
        return True
                