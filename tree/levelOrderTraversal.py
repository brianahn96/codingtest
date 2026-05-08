# Overall Time Complexity: O(N)
# Overall Space Complexity: O(W) where W is the maximum width of the tree

# Source URL for the problem description
# https://www.geeksforgeeks.org/problems/level-order-traversal/1

# Define the Node class representing a node in a binary tree
class Node:
    # Initialize a new Node with a given value
    def __init__(self, value):
        # Assign the value to the node's data
        self.data = value
        # Initialize the left child as None
        self.left = None
        # Initialize the right child as None
        self.right = None

# Function to perform level-order traversal of a binary tree
def levelOrder(root):
    # Import deque from the collections module for efficient queue operations
    from collections import deque
    # Initialize the result list to store levels
    res = []
    # If the root is None, return an empty result list
    if not root:
        # Return empty list
        return res
        
    # Initialize a queue for BFS with the root node
    queue = deque([root])
    
    # Process nodes level by level
    while queue:
        # Initialize a list to store values at the current level
        values = []
        # Iterate over the number of nodes at the current level
        for _ in range(len(queue)):
            # Dequeue the next node
            node = queue.popleft()
            # Append the node's data to the current level's value list
            values.append(node.data)
            
            # If a left child exists
            if node.left:
                # Enqueue the left child for the next level
                queue.append(node.left)
            # If a right child exists
            if node.right:
                # Enqueue the right child for the next level
                queue.append(node.right)
        # Append the current level's values to the result list
        res.append(values)
        
    # Return the list of levels
    return res
