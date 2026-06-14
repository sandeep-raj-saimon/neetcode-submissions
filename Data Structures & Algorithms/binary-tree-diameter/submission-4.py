# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans = 0

    def findDiameter(self, root):
        if root is None:
            return 0

        left = self.findDiameter(root.left)
        right = self.findDiameter(root.right)

        diameter = left + right
        self.ans = max(self.ans, diameter)

        return  (1 + max(left, right))
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        self.findDiameter(root)
        return self.ans
        