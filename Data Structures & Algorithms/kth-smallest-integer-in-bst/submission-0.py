# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.path = []
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inOrder(root):
            if root is None:
                return

            inOrder(root.left)
            self.path.append(root.val)
            inOrder(root.right)
        inOrder(root)
        return self.path[k-1]