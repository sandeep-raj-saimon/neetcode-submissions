# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans = 1
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        def findMaxDepth(root, level=1):
            if root is None:
                return
            self.ans = max(self.ans, level)
            if root.right is not None:
                findMaxDepth(root.right, level+1)
            if root.left is not None:
                findMaxDepth(root.left, level+1)
            return
        
        findMaxDepth(root)
        return self.ans
        