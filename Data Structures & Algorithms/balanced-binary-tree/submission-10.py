# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.is_balanced = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def check(root):
            if root is None:
                return 0
            left = check(root.left)
            right = check(root.right)
            if abs(left - right) > 1:
                self.is_balanced = False
            return max(left+1, right+1)

        check(root)
        return self.is_balanced