from collections import defaultdict
class Solution:
    def __init__(self):
        self.order = []
        self.possible = True
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        visited = [0 for _ in range(numCourses)]
        path = [0 for _ in range(numCourses)]

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

            for neighbour in adj[i]:
                dfs(neighbour)
            path[i] = 0
            self.order.append(i)
        for i in range(numCourses):
            if visited[i] == 0:
                dfs(i)
        return self.order if self.possible else []