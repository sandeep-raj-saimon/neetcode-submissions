# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans = float('-inf')
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        def findDepth(root, count=0):
            if root is None:
                return
            count+=1
            self.ans = max(self.ans, count)
            findDepth(root.left, count)
            findDepth(root.right, count)
        findDepth(root)
        return self.ans