from collections import defaultdict
class Solution:
    def __init__(self):
        self.isCycle = False
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        total number of components is 1, and there is no cycle
        """
        count = 0
        adj = defaultdict(list)
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        visited = [0 for _ in range(n)]
        def dfs(i, parent=-1):
            visited[i] = 1

            for n in adj[i]:
                if visited[n] == 0:
                    dfs(n, i)
                else:
                    if n == parent:
                        pass
                    else:
                        self.isCycle = True
                        return
        
        for i in range(n):
            if visited[i] == 0:
                count+=1
                # if count > 1:
                #     return False
                dfs(i)

        return (count == 1 and not self.isCycle)