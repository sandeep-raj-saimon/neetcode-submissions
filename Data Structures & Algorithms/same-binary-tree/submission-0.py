class Solution:
    def preOrderTraversal(self, root, arr):
        if not root:
            arr.append(None)
            return None
        print(root.val)
        arr.append(root.val)
        self.preOrderTraversal(root.left, arr)
        self.preOrderTraversal(root.right, arr)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        arr1 = []
        arr2 = []
        self.preOrderTraversal(p, arr1)
        self.preOrderTraversal(q, arr2)
        return arr1 == arr2