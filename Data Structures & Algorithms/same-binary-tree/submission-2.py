# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preOrder(self, root, arr):
        if root is None:
            arr.append(None)
            return

        arr.append(root.val)
        self.preOrder(root.left, arr)
        self.preOrder(root.right, arr)
        return arr


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        arr_p = self.preOrder(p, [])
        arr_q = self.preOrder(q, [])

        return arr_p == arr_q