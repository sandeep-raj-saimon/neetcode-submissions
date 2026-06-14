# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        use the property of binary search tree
        left -> smaller
        right -> larger
        if a node is smaller 
        """

        # always keep p as small
        if p.val > q.val:
            p, q = q, p
        def recursion(root):
            if root is None:
                return

            if p.val <= root.val <= q.val:
                return root
            elif q.val > root.val:
                return recursion(root.right)
            else:
                return recursion(root.left)
 
        return recursion(root)