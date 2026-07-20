class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None  # If the root is None, return None
        if root == p or root == q:
            return root  # If the current node is either p or q, return it
        left = self.lowestCommonAncestor(root.left, p, q)  # Recur on the left subtree
        right = self.lowestCommonAncestor(root.right, p, q)  # Recur on the right subtree
        if left and right:
            return root  # If both left and right are not None, current node is the LCA
        if left:
            return left  # If only left is not None, return left
        return right  # If only right is not None, return right
    # Example usage
tree = TreeNode(3)
tree.left = TreeNode(5)
tree.right = TreeNode(1)
p = tree.left
q = tree.right
lca = tree.lowestCommonAncestor(tree, p, q)
print(lca.val)  # Output: 3
