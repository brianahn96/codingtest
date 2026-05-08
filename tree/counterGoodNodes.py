# Overall Time Complexity: O(N)
# Overall Space Complexity: O(W) where W is the maximum width of the tree

# Source URL for the problem description
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/

# Define the TreeNode class representing a node in a binary tree
class TreeNode:
    # Initialize a new TreeNode with value, left child, and right child
    def __init__(self, val=0, left=None, right=None):
        # Assign the value to the node
        self.val = val
        # Assign the left child to the node
        self.left = left
        # Assign the right child to the node
        self.right = right
        
# Import deque from the collections module for efficient queue operations
from collections import deque

# Function to count "good" nodes where all values on path from root are less or equal
def goodNodes(root: TreeNode) -> int:
    # Initialize the count of good nodes
    count = 0
    # Initialize a deque for breadth-first search
    queue = deque()
    # Append the root and its value (as the current max) to the queue
    queue.append((root, root.val))

    # Iterate as long as there are nodes in the queue
    while queue:
        # Dequeue the next node and the maximum value encountered on its path
        node, value = queue.popleft()
        # Check if the current node's value is greater than or equal to the path's maximum
        if node.val >= value:
            # Increment the good nodes count
            count += 1
        # Update the maximum value for the children's paths
        max_val = max(node.val, value)
        # If the left child exists
        if node.left:
            # Enqueue the left child and the updated maximum value
            queue.append((node.left, max_val))
        # If the right child exists
        if node.right:
            # Enqueue the right child and the updated maximum value
            queue.append((node.right, max_val))
    # Return the total count of good nodes
    return count
