# Definition for a Binary Tree Node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val          # Value of the node
        self.left = left        # Left child
        self.right = right      # Right child


class Solution:
    def __init__(self):
        # 'prev' stores the previously processed node.
        # Initially there is no previous node.
        self.prev = None

    def flatten(self, root):
        """
        Flatten the binary tree into a linked list in-place.

        The linked list should follow Preorder Traversal:
        Root -> Left -> Right

        We solve it using Reverse Preorder:
        Right -> Left -> Root
        """

        # Base Case
        if root is None:
            return

        # Step 1:
        # First flatten the RIGHT subtree.
        # We process right first because we are building the linked list
        # from the end towards the beginning.
        self.flatten(root.right)

        # Step 2:
        # Then flatten the LEFT subtree.
        self.flatten(root.left)

        # Step 3:
        # Connect the current node to the previously processed node.
        #
        # Example:
        # If prev is node 5,
        # then current node 2 becomes:
        #
        # 2 -> 5
        #
        root.right = self.prev

        # Step 4:
        # Since the tree must become a linked list,
        # remove the left child.
        root.left = None

        # Step 5:
        # Update prev to the current node.
        # This node will become the "next" node for its parent.
        self.prev = root


# -------------------------------
# Creating the Binary Tree
# -------------------------------

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(5)

root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

"""
Original Tree

          1
        /   \
       2     5
      / \   / \
     3   4 6   7
"""


# -------------------------------
# Flatten the Tree
# -------------------------------

obj = Solution()
obj.flatten(root)


# -------------------------------
# Print the Flattened Linked List
# -------------------------------

curr = root

print("Flattened Tree:")

while curr:
    print(curr.val, end=" -> ")
    curr = curr.right

print("None")
'''tc: O(n) because we visit each node once
sc: O(h) where h is the height of the tree, due to the recursion stack
'''