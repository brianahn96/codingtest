# Overall Time Complexity: O(N)
# Overall Space Complexity: O(H) where H is the tree height

# Source URL for the problem description
# https://leetcode.com/problems/range-sum-of-bst/description/

# Import Optional from typing for type hinting
from typing import Optional

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

# Recursive function to calculate the range sum in a BST
def rangeSumBSTRecursive(root: Optional[TreeNode], low: int, high: int) -> int:
    # Check if the current node is None
    if not root:
        # Return 0 for an empty node
        return 0
    
    # Calculate current node's contribution if its value is within the range [low, high]
    sum_val = root.val if low <= root.val <= high else 0
    # Add the range sum of the left subtree
    sum_val += rangeSumBSTRecursive(root.left, low, high)
    # Add the range sum of the right subtree
    sum_val += rangeSumBSTRecursive(root.right, low, high)
    # Return the total sum
    return sum_val

# Optimized DFS function to calculate range sum by pruning subtrees
def rangeSumBSTDFS(root: Optional[TreeNode], low: int, high: int) -> int:
    
    # Define a DFS helper function
    def dfs(node):
        # Check if the current node is None
        if not node:
            # Return 0
            return 0
        
        # If node value is less than low, the left subtree can be skipped
        if node.val < low:
            # Only search in the right subtree
            return dfs(node.right)
        # If node value is greater than high, the right subtree can be skipped
        elif node.val > high:
            # Only search in the left subtree
            return dfs(node.left)
        # If node value is within range, include it and search both subtrees
        return node.val + dfs(node.left) + dfs(node.right)
    
    # Start the DFS traversal from the root
    return dfs(root)

# Iterative function using a stack to calculate the range sum
def rangeSumBSTDFSSum(root: Optional[TreeNode], low: int, high: int) -> int:
    # Initialize a stack with the root node and a sum variable at 0
    stack, sum_val = [root], 0
    
    # Process nodes as long as the stack is not empty
    while stack:
        # Pop the next node from the stack
        node = stack.pop()
        # If the node is not None
        if node:
            # If the current value is greater than low, the left child might be in range
            if node.val > low:
                # Push the left child onto the stack
                stack.append(node.left)
            # If the current value is less than high, the right child might be in range
            if node.val < high:
                # Push the right child onto the stack
                stack.append(node.right)
            # If the current node's value is within the [low, high] range
            if low <= node.val <= high:
                # Add its value to the cumulative sum
                sum_val += node.val
    # Return the total range sum
    return sum_val
