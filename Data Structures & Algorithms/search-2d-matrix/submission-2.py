class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        col = len(matrix[0])-1

        while (row < len(matrix) and 0 <= col < len(matrix[0])):
            if matrix[row][col] == target:
                return True
            elif target > matrix[row][col]:
                row += 1
            else:
                col -= 1
            print(row,col)
        return False