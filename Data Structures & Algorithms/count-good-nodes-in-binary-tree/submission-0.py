# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        generate all paths, and in path if max_element is greater than element, then dont include the element
        """
        ans = []
        def dfs(root, max_element = float('-inf')):
            if root is None:
                return
            print("here", root.val, max_element)
            if root.val >= max_element:
                ans.append(root.val)
            
            max_element = max(max_element, root.val)
            if root.right:
                dfs(root.right, max_element)
            
            if root.left:
                dfs(root.left, max_element)
            return

        dfs(root)
        print(ans)
        return len(ans)
        
        