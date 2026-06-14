# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # time complexity is O(n^2) as there are n nodes, and hence n recursive calls
        # and in each call, there is indexing and slicing which O(n)
        # so n*n => O(n^2)
        # def recursion(pre_order, in_order):
        #     if not pre_order or not in_order:
        #         return
        #     print(pre_order)
        #     root = TreeNode(pre_order[0])
        #     mid = in_order.index(pre_order[0])
        #     root.left = recursion(pre_order[1 : mid+1], in_order[:mid])
        #     root.right = recursion(pre_order[mid+1:], in_order[mid+1:])
        #     return root

        # return recursion(preorder, inorder)

        # lets try to optimize the space, by which dictionary

        indices = {val: idx for idx, val in enumerate(inorder)}

        def recursion(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return None

            root = TreeNode(preorder[pre_start])
            index = indices.get(preorder[pre_start])

            left_tree_size = index - in_start
            root.left = recursion(pre_start +1, pre_start + left_tree_size, in_start, index-1)
            root.right = recursion(pre_start + left_tree_size+1, pre_end, index+1, in_end)

            return root

        return recursion(0, len(preorder)-1, 0, len(inorder)-1)
