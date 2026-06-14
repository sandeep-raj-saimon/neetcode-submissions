# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_depth = 0
    def findDiameter(self, root):
        if not root:
            return 0
        left = self.findDiameter(root.left)
        right = self.findDiameter(root.right)
    
        self.max_depth = max(self.max_depth, left + right)
        return 1 + max(left, right)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root:
            self.findDiameter(root)
            return self.max_depth
        return 0