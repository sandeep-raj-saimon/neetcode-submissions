# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if not p or not q:
        #     return False

        def findAns(p, q):
            if p is None and q is None:
                return True


            if p and q and p.val == q.val and findAns(p.left, q.left) and findAns(p.right, q.right):
                return True
            else:
                return False
        return findAns(p, q)
        