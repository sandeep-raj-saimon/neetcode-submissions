class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        row = len(grid)
        col = len(grid[0])
        max_area = 0
        area = 0

        def dfs(i, j):
            if (i < 0 or i >= row or j < 0 or j >= col):
                return 0

            if grid[i][j] == 0 or visited[i][j] == True:
                return 0
            visited[i][j] = True
            area = 1
            directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
            for d in directions:
                print(i, j, d)
                area += dfs(i+d[0], j+d[1])
            return area
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == 1 and visited[i][j] == False:
                    area = dfs(i, j)
                    max_area = max(area, max_area)
        return max_area