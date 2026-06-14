from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        def dfs(i, parent=-1):
            visited[i] = True

            for neighbour in adj[i]:
                if visited[neighbour]:
                    if parent != neighbour:
                        return True  # Cycle detected
                else:
                    if dfs(neighbour, i):
                        return True
            return False

        for edge in edges:
            visited = [False] * (len(edges) + 1)

            # Add the current edge to the adjacency list
            u, v = edge
            adj[u].append(v)
            adj[v].append(u)

            # Check if adding this edge creates a cycle
            if dfs(u):
                return edge

        return []
