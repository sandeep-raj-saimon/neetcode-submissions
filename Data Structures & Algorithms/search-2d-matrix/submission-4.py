class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        left = col-1
        top = 0
        while (left >= 0 and top < row ):
            print("dasds")
            if matrix[top][left] == target:
                return True
            elif target < matrix[top][left]:
                print("ehre")
                left-=1
            else:
                print("dasdas")
                top+=1
            
            
        return False