class Solution:
    def __init__(self):
        self.max_count = 0
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_count = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0 or visited[i][j] == 1:
                return 0
            visited[i][j] = 1
            area = 1
            directions = [[0,1], [0,-1], [1,0], [-1,0]]
            for direction in directions:
                area += dfs(i + direction[0], j + direction[1])
            return area
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    area = dfs(i, j)
                    self.max_count = max(area, self.max_count)
        return self.max_count