from collections import deque


# Create a TreeNode class
class TreeNode:
    def __init__(self, val=0):
        self.val = val          # Store the value of the node
        self.left = None        # Store the left child
        self.right = None       # Store the right child


# Create Solution class
class Solution(object):

    def zigzagLevelOrder(self, root):
        # If tree is empty, return empty list
        if root is None:
            return []

        # Store the final answer
        result = []

        # Add root node to the queue
        queue = deque([root])

        # True means Left → Right
        # False means Right → Left
        left_to_right = True

        # Continue until queue becomes empty
        while queue:
            # Store current level values
            level = []

            # Number of nodes in current level
            level_size = len(queue)

            # Process all nodes in current level
            for i in range(level_size):
                # Remove first node from queue
                node = queue.popleft()

                # Add current node value to level
                level.append(node.val)

                # If left child exists, add it to queue
                if node.left:
                    queue.append(node.left)

                # If right child exists, add it to queue
                if node.right:
                    queue.append(node.right)

            # If direction is Right → Left
            if left_to_right == False:
                # Reverse current level
                level.reverse()

            # Add current level to final result
            result.append(level)

            # Change the direction
            left_to_right = not left_to_right

        # Return final answer
        return result


# ---------------- EXAMPLE USAGE ----------------

# Create root node with value 1
root = TreeNode(1)

# Create node 2 as left child of node 1
root.left = TreeNode(2)

# Create node 3 as right child of node 1
root.right = TreeNode(3)

# Create node 4 as left child of node 2
root.left.left = TreeNode(4)

# Create node 5 as right child of node 2
root.left.right = TreeNode(5)

# Create node 6 as left child of node 3
root.right.left = TreeNode(6)

# Create node 7 as right child of node 3
root.right.right = TreeNode(7)


# Call the function and print the answer
print(Solution().zigzagLevelOrder(root))


# Output:
# [[1], [3, 2], [4, 5, 6, 7]]


'''
Time Complexity: O(n)

n = number of nodes in the binary tree.

We visit every node exactly once.


Space Complexity: O(n)

In the worst case, the queue may store many nodes
from one level of the binary tree.
'''