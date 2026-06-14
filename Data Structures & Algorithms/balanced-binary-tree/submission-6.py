# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans = True
    def check(self, root):
        if root is None:
            return 0
        
        left = self.check(root.left)
        right = self.check(root.right)

        if abs(left - right) > 1:
            self.ans = False
        height = max(left, right)
        return 1 + height
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # check at every point whether tree is balanced or not
        if root is None:
            return True
        self.check(root)
        return self.ans
