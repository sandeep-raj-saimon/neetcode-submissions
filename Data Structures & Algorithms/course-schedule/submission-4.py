from collections import defaultdict
class Solution:
    def __init__(self):
        self.possible = True
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        we need to detect cycle
        if cycle exists then we know that courses can not be finished
        else it can be finished
        """
        visited = path = [0 for _ in range(numCourses)]
        adj = defaultdict(list)
        for p in prerequisites:
            adj[p[0]].append(p[1])
        # print(adj)
        def dfs(i):
            if path[i] == 1:
                self.possible = False
                return
                    
            # if visited[i] == 1:
            #     return
            visited[i] = 1
            path[i] = 1
            for neighbour in adj[i]:
                print('neighbour is ', neighbour)
                # dont check for visited[neighbour], otherwise we wont be able to find the cycle
                dfs(neighbour)

            # after we have traversed all the neighbours, it is not part of the path anymore
            # hence mark it as unvisited
            path[i] = 0
        
        for i in range(numCourses):
            if visited[i] == 0:
                dfs(i)
        return self.possible