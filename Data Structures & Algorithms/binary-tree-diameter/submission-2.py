class Solution:
    def __init__(self):
        self.max_diameter = 0

    def depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Recursively find the depth of the left and right subtrees
        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)
        
        # Calculate the diameter passing through the current node
        self.max_diameter = max(self.max_diameter, left_depth + right_depth)
        
        # Return the depth of the current subtree
        return 1 + max(left_depth, right_depth)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.depth(root)
        return self.max_diameter