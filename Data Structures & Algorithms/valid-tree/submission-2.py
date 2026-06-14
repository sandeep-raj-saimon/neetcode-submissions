from collections import defaultdict
class Solution:
    def __init__(self):
        self.isCycle = False
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        visited =[0 for _ in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        count = 0

        def dfs(i, parent = -1):
            if visited[i] == 1:
                self.isCycle = True
                return
            visited[i] = 1
            for neighbour in adj[i]:
                if parent != neighbour:
                    dfs(neighbour, i)

        for i in range(n):
            if visited[i] == 0:
                count+=1
                if count > 1:
                    return False
                dfs(i, -1)
        return  not self.isCycle