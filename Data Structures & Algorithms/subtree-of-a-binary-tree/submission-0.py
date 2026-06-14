# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans = False
    def sameTree(self, p, q):
        if not p and not q:
            return True
        
        if p and q and p.val == q.val:
            return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)
        else:
            return False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        if not root or not subRoot:
            return False

        def traverse(root):
            if not root:
                return
            
            curr_ans = self.sameTree(root, subRoot)
            if curr_ans:
                self.ans = True
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        return self.ans