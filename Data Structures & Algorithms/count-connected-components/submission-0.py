from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [0 for _ in range(n)]
        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        def dfs(i):
            visited[i] = 1

            for neighbour in adj[i]:
                if not visited[neighbour]:
                    dfs(neighbour)
        
        count = 0
        for i in range(n):
            if not visited[i]:
                count+=1
                dfs(i)
        return count