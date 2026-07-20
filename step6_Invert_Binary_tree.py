class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def invertTree(self, root):

        if root is None:
            return None

        # Swap children
        root.left, root.right = root.right, root.left

        # Invert left subtree
        self.invertTree(root.left)

        # Invert right subtree
        self.invertTree(root.right)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end=" ")
            self.inorder(root.right)


# Example
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print("Original Tree (Inorder):")
root.inorder(root)

root = root.invertTree(root)

print("\nInverted Tree (Inorder):")
root.inorder(root)