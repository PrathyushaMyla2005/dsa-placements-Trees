
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def avg(root):
        if not root: #return 0 if the root is None
            return 0
        result = [] # List to store the average of each level
        queue = deque([root]) # Initialize a queue with the root node
        while queue: # While there are nodes in the queue
            level_size = len(queue) # Get the number of nodes at the current level
            level_sum = 0 # Initialize the sum of the current level
            for i in range(level_size): # Iterate through all nodes at the current level
                node = queue.popleft() # Remove the first node from the queue
                level_sum += node.val # Add the value of the current node to the level sum
                if node.left: # If the left child exists, add it to the queue
                    queue.append(node.left)
                if node.right: # If the right child exists, add it to the queue
                    queue.append(node.right)
            average = level_sum / level_size # Calculate the average for the current level
            result.append(average) # Append the average to the result list
        return result # Return the list of averages for each level
        #example usage
if __name__ == "__main__":  
    # Create a binary tree
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # Call the avg function and print the result
    averages = TreeNode.avg(root)
    print(averages)  # Output: [3.0, 14.5, 11.0]
'''tc: O(n) time | O(w) space where n is the number of nodes and w is the maximum width of the tree
'''