# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.depth = float('-inf')
    def findDepth(self, root, depth):
        self.depth = max(self.depth, depth)
        if root.right:
            depth_right = self.findDepth(root.right, depth+1)
        if root.left:
            depth_left = self.findDepth(root.left, depth+1)
        return depth
       
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            self.findDepth(root, 1)
            return self.depth
        return 0
        
        