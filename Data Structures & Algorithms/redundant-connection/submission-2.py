from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        def isCycle(i, parent=-1):
            visited[i] = True

            for neighbour in adj[i]:
                if visited[neighbour]:
                    if neighbour != parent:
                        return True
                else:
                    if isCycle(neighbour, i):
                        return True
            return False
        
        """
        we will keep on adding the edge, if on adding edge we get cycle
        we return edge
        """
        for edge in edges:
            visited = [False for _ in range(len(edges)+1)]

            u,v = edge
            adj[u].append(v)
            adj[v].append(u)

            if isCycle(u):
                return edge
        return []
