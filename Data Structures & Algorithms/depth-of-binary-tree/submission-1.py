# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans = 0
    def findDepth(self, root, depth=1):
        self.ans = max(self.ans, depth)
        if root.right:
            self.findDepth(root.right, depth+1)
        if root.left:
            self.findDepth(root.left, depth+1)
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        self.findDepth(root)
        return self.ans
        

        

        