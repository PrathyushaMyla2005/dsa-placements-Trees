from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def are_cousins(root, x, y):
        if not root:  # If the root is None, return False
            return False

        queue = deque([(root, None)])  # Initialize a queue with the root node and its parent as None
        x_parent = y_parent = None  # Variables to store the parents of x and y
        x_depth = y_depth = -1  # Variables to store the depths of x and y
        depth = 0  # Initialize depth

        while queue:  # While there are nodes in the queue
            level_size = len(queue)  # Get the number of nodes at the current level
            for i in range(level_size):  # Iterate through all nodes at the current level
                node, parent = queue.popleft()  # Remove the first node from the queue along with its parent

                if node.val == x:  # If the current node's value is x
                    x_parent = parent  # Store its parent
                    x_depth = depth  # Store its depth

                if node.val == y:  # If the current node's value is y
                    y_parent = parent  # Store its parent
                    y_depth = depth  # Store its depth

                if node.left:  # If the left child exists, add it to the queue with current node as parent
                    queue.append((node.left, node))
                if node.right:  # If the right child exists, add it to the queue with current node as parent
                    queue.append((node.right, node))

            depth += 1  # Increment depth after processing all nodes at the current level

        return (x_depth == y_depth) and (x_parent != y_parent)  # Return True if x and y are cousins
    #EXAample usage
if __name__ == "__main__":
    # Create a binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    # Check if nodes 4 and 6 are cousins
    result = TreeNode.are_cousins(root, 4, 6)
    print(result)  # Output: True

    # Check if nodes 5 and 6 are cousins
    result = TreeNode.are_cousins(root, 5, 6)
    print(result)  # Output: False
'''tc: O(n) time | O(w) space where n is the number of nodes and w is the maximum width of the tree'''