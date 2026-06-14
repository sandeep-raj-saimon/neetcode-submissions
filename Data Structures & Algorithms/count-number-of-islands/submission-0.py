class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        rows, cols = len(grid), len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == "0" or visited[i][j] == 1:
                return
            visited[i][j] = 1
            # we need to move all four directions
            directions = [[0,1], [0,-1], [1,0], [-1,0]]
            for direction in directions:
                dfs(i+direction[0], j+direction[1])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    count+=1
                    dfs(i,j)
        return count