# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def findAns(root):
            # if not self.ans:
            #     return 
            if root is None or not self.ans:
                return 0

            left = findAns(root.left)
            right = findAns(root.right)

            if abs(left - right) > 1:
                self.ans = False

            return max(left, right) + 1

        findAns(root)
        return self.ans

            
        