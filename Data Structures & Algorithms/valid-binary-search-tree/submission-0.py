# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.inorder = []
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def traverse(root):
            if not root:
                return
            traverse(root.left)
            self.inorder.append(root.val)
            traverse(root.right)
        traverse(root)
        for i in range(1,len(self.inorder)):
            if self.inorder[i-1] >= self.inorder[i]:
                return False
        return True