class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        fresh = 0 # to keep track of all the fresh fruits
        q = []
        initial = []
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    visited[i][j] = 1
                    initial.append([i,j])
                elif grid[i][j] == 1:
                    fresh +=1
        if len(initial):
            q.append(initial)
        time = 0
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        while len(q) and fresh > 0:
            stales = q.pop(0)
            new_stales = []
            for stale in stales:
                for direction in directions:
                    i = stale[0] + direction[0]
                    j = stale[1] + direction[1]
                    # print(i,j)
                    if i >= 0 and j >= 0 and i < rows and j < cols and grid[i][j] == 1 and visited[i][j] == 0:
                        visited[i][j]=1
                        new_stales.append([i,j])
                        fresh -=1
            if len(new_stales):
                q.append(new_stales)
            time+=1

        return time if fresh <= 0 else -1