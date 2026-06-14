from collections import defaultdict
class Solution:
    def __init__(self):
        self.possible = True
        self.order = []
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = [0 for _ in range(numCourses)]
        path = [0 for _ in range(numCourses)]
        adj = defaultdict(list)

        for p in prerequisites:
            adj[p[0]].append(p[1])
        def dfs(i):
            if path[i] == 1:
                self.possible = False
                return

            if visited[i] == 1:
                return
            visited[i] = 1
            path[i] = 1

            for n in adj[i]:
                dfs(n)
            path[i] = 0
            self.order.append(i)

        for i in range(numCourses):
            if visited[i] == 0:
                dfs(i)
        return self.order if self.possible else []
