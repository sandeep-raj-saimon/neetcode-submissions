# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        q = [[root]]

        while len(q) != 0:
            print(q)
            elements = q.pop(0)
            children = []
            children_val = []
            for ele in elements:
                children_val.append(ele.val)
                if ele.left:
                    children.append(ele.left)
                if ele.right:
                    children.append(ele.right)
            if len(children) != 0:
                q.append(children)
            if len(children_val) != 0:
                ans.append(children_val)
        print(ans)
        return ans