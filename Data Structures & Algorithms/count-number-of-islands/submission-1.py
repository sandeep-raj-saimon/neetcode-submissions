class Solution:
    def __init__(self):
        self.visited = None
        self.grid = None
        self.rows = None
        self.col = None

    def dfs(self, i, j):
        if (i < 0 or i >= self.rows or j < 0 or j >= self.col):
            return
        if (self.grid[i][j] == "0" or self.visited[i][j] == True):
            return
        self.visited[i][j] = True
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        for d in directions:
            self.dfs(i+d[0], j+d[1])

    def numIslands(self, grid: List[List[str]]) -> int:
        self.rows = len(grid)
        self.col = len(grid[0])
        self.grid = grid
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        self.visited = visited

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if visited[i][j] == False and grid[i][j] == "1":
                    count+=1
                    self.dfs(i, j)
        return count