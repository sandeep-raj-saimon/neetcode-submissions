class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = {}
        col_map = {}
        for i in range(9):
            row_map[i] = []
            col_map[i] = []

        row_col_map = [[[] for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    pass
                else:
                    board[i][j] = int(board[i][j])
                    if board[i][j] not in row_map[i]:
                        row_map[i].append(board[i][j])
                    else:
                        return False

                    if board[i][j] not in col_map[j]:
                        col_map[j].append(board[i][j])
                    else:
                        return False
                    
                    row_i = i//3
                    col_j = j//3
                    if board[i][j] not in row_col_map[row_i][col_j]:
                        row_col_map[row_i][col_j].append(board[i][j])
                    else:
                        return False

        return True