# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
        
    def __init__(self):
        self.ans = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0
            left = height(root.left)
            right = height(root.right)

            if abs(left - right) > 1:
                self.ans = False
            return 1 + max(left, right)
        if not root:
            return True
        left = height(root.right)
        right = height(root.left)
        if abs(left - right) > 1:
            self.ans = False
        return self.ans
        