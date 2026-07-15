from collections import deque  # Import deque to use it as a queue


# Define the TreeNode class to create binary tree nodes
class TreeNode:
    def __init__(self, val=0):
        self.val = val          # Store the value of the node
        self.left = None        # Store the left child of the node
        self.right = None       # Store the right child of the node


# Function to perform level order traversal of a binary tree
def level_order_traversal(root):

    # If the tree is empty, return an empty list
    if not root:
        return []

    # Create an empty list to store the final result
    result = []

    # Create a queue and initially add the root node
    queue = deque([root])

    # Continue until the queue becomes empty
    while queue:

        # Create an empty list to store nodes of the current level
        level = []

        # Store the number of nodes present in the current level
        level_size = len(queue)

        # Process all nodes of the current level
        for i in range(level_size):

            # Remove the first node from the queue
            node = queue.popleft()

            # Add the current node value to the level list
            level.append(node.val)

            # Check if the current node has a left child
            if node.left:

                # Add the left child to the queue
                queue.append(node.left)

            # Check if the current node has a right child
            if node.right:

                # Add the right child to the queue
                queue.append(node.right)

        # Add the completed current level to the final result
        result.append(level)

    # Return the final level order traversal result
    return result


# Create the root node with value 1
root = TreeNode(1)

# Create node 2 as the left child of node 1
root.left = TreeNode(2)

# Create node 3 as the right child of node 1
root.right = TreeNode(3)

# Create node 4 as the left child of node 2
root.left.left = TreeNode(4)

# Create node 5 as the right child of node 2
root.left.right = TreeNode(5)


# Call the level order traversal function and print the result
print(level_order_traversal(root))


# Output:
# [[1], [2, 3], [4, 5]]


# Time Complexity: O(n)
# We visit every node exactly once.

# Space Complexity: O(n)
# In the worst case, the queue may store many nodes of one level.