# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.right_view = []
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = [[root]]
        while len(q) != 0:
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
                self.right_view.append(children_val[-1])
        return self.right_view

        