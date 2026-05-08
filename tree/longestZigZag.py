# Overall Time Complexity: O(N)
# Overall Space Complexity: O(H) where H is the tree height

# Source URL for the problem description
# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/

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
        
# Import Optional from typing for type hinting
from typing import Optional

# Function to calculate the longest ZigZag path using recursion
def longestZigZagRecursive(root: Optional[TreeNode]) -> int:
    # Initialize the maximum length of the ZigZag path
    max_length = 0

    # Define a DFS helper function
    def dfs(node, is_right, length):
        # Access the max_length variable from the outer scope
        nonlocal max_length

        # Check if the current node is None
        if not node:
            # Return as there is nothing to process
            return

        # Update the maximum length found so far
        max_length = max(max_length, length)

        # If the last step was to a right child
        if is_right:
            # Continue the ZigZag by going right (length + 1)
            dfs(node.right, False, length + 1)
            # Or start a new ZigZag path by going left
            dfs(node.left, True, 1)
        # If the last step was to a left child
        else:
            # Continue the ZigZag by going left (length + 1)
            dfs(node.left, True, length + 1)
            # Or start a new ZigZag path by going right
            dfs(node.right, False, 1)
        
    # Start DFS from the root assuming the previous move was from the right
    dfs(root, True, 0)
    # Start DFS from the root assuming the previous move was from the left
    dfs(root, False, 0)
    # Return the maximum ZigZag length found
    return max_length


# Function to calculate the longest ZigZag path using an iterative stack
def longestZigZagStack(root: Optional[TreeNode]) -> int:
    # Check if the root node is None
    if not root:
        # Return 0 for an empty tree
        return 0
    # Initialize a stack with the root and initial left/right path lengths
    stack = [(root, 0, 0)]
    # Initialize the maximum length
    max_length = 0
    # Process nodes as long as the stack is not empty
    while stack:
        # Pop the next node and its current path lengths
        node, left, right = stack.pop()
        # Update the maximum length with current path values
        max_length = max(max_length, left, right)
        # If a left child exists
        if node.left:
            # Push the left child with an incremented right path length (zigzag)
            stack.append((node.left, right + 1, 0))
        # If a right child exists
        if node.right:
            # Push the right child with an incremented left path length (zigzag)
            stack.append((node.right, 0, left + 1))
    # Return the total maximum ZigZag length found
    return max_length
