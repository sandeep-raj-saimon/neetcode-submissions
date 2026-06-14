from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0  # To keep track of fresh oranges
        q = deque()  # Use deque for efficient queue operations
        
        # Collect initial rotten oranges and count fresh ones
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))  # Add all rotten oranges to the queue
                elif grid[i][j] == 1:
                    fresh += 1  # Count fresh oranges

        time = 0
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        # Perform BFS to spread the rot
        while q and fresh > 0:
            for _ in range(len(q)):  # Process all rotten oranges at the current level
                x, y = q.popleft()
                for direction in directions:
                    new_x, new_y = x + direction[0], y + direction[1]
                    if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == 1:
                        # Rot the fresh orange and add it to the queue
                        grid[new_x][new_y] = 2
                        fresh -= 1
                        q.append((new_x, new_y))
            time += 1  # Increment time after processing one level

        # If there are still fresh oranges left, return -1
        return time if fresh == 0 else -1
