class Solution:
    def __init__(self):
        self.count = 0

    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = [[False for _ in range(col)] for _ in range(row)]
        directions = [[0,1], [0,-1], [1,0], [-1,0]] 
        count = 0

        def dfs(i, j):
            visited[i][j] = True
            for direction in directions:
                dx, dy = direction
                new_x, new_y = i+dx, j+dy
                if new_x >= 0 and new_x < row and new_y >= 0 and new_y < col and grid[new_x][new_y] == "1" and visited[new_x][new_y] == False:
                    dfs(new_x, new_y)


        for i in range(row):
            for j in range(col):
                if visited[i][j] == False and grid[i][j] == "1":
                    dfs(i,j)
                    count+=1
        return count