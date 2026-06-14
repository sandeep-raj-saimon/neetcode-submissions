# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        """
        if p.val > q.val:
            p,q = q,p

        def find(root):
            if root is None:
                return

            val = root.val
            if p.val <= val <= q.val:
                return root

            return find(root.left) or find(root.right)
        
        return find(root)