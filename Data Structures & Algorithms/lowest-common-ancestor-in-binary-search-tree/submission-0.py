# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findpath(self, root, path, node):
        if not root:
            return
        path.append(root)
        if node.val == root.val:
            return
        if node.val > root.val:
            self.findpath(root.right, path, node)
        else:
            self.findpath(root.left, path, node)
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        path1 = []
        path2 = []

        self.findpath(root, path1, p)
        self.findpath(root, path2, q)

        i = len(path1)-1
        j = len(path2)-1
        print(path1, path2)
        # return p
        for node in path1[::-1]:
            if node in path2:
                return node
        

