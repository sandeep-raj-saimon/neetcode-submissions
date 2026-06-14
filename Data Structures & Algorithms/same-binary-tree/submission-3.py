# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # can be done through traversal
        # and also through recursion
        if not p and not q:
            return True

        if p and q and p.val == q.val and self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left):
            return True
        else:
            return False