"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
import copy
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        new = {}
        def dfs(node):
            if node in new:
                return new[node]

            newnode = Node(node.val)
            new[node] = newnode
            neighbours = node.neighbors

            for neighbour in neighbours:
                newnode.neighbors.append(dfs(neighbour))
            return newnode
        print(new)
        return dfs(node) if node else None