# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def findDiameter(root):
            if root is None:
                return 0

            left = findDiameter(root.left)
            right = findDiameter(root.right)
            self.ans = max(self.ans, left+ right)
            return max(left, right) + 1
        
            
        findDiameter(root)
        return self.ans