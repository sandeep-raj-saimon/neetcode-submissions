class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        visited = [[False for _ in range(col)] for _ in range(row)]
        q = []
        fresh = 0
        initial_rotten = []
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    fresh+=1
                if grid[i][j] == 2:
                    initial_rotten.append([i,j])
                    visited[i][j] = True

        if len(initial_rotten) > 0:
            q.append(initial_rotten)

        # if len(initial_rotten) == 0:
        #     return -1

        time = 0
        directions = [[0, 1], [0,-1], [1,0], [-1, 0]]
        while q and fresh > 0:
            stales = q.pop(0)

            new_stales = []
            for stale in stales:
                x, y = stale

                for direction in directions:
                    dx, dy = direction

                    new_x = x+dx
                    new_y = y+dy

                    if (new_x >= 0
                        and new_x < row
                        and new_y >= 0
                        and new_y < col
                        and grid[new_x][new_y] == 1
                        and visited[new_x][new_y] == False):
                        visited[new_x][new_y] = True
                        new_stales.append([new_x, new_y])
                        fresh-=1

            if len(new_stales) > 0:
                q.append(new_stales)
            time+=1
        return time if fresh <=0 else -1


        