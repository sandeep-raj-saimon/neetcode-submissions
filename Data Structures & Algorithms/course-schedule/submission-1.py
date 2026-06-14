from collections import defaultdict
class Solution:
    def __init__(self):
        self.possible = True
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [0 for _ in range(numCourses)]
        path = [0 for _ in range(numCourses)]
        adj = defaultdict(list)

        for prerequisite in prerequisites:
            adj[prerequisite[0]].append(prerequisite[1])
        print(adj)
        def dfs(i):
            if path[i] == 1:
                self.possible = False
                return
            if visited[i] == 1:
                return
            visited[i] = 1
            path[i] = 1
            neighbours = adj[i]
            for neighbour in neighbours:
                dfs(neighbour)
            path[i] = 0
        for i in range(numCourses):
            if visited[i] == 0:
                dfs(i)
        return self.possible
        