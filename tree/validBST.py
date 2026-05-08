# Overall Time Complexity: O(N)
# Overall Space Complexity: O(H) where H is the tree height

# Source URL for the problem description
# https://leetcode.com/problems/validate-binary-search-tree/description/

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
        
# Function to determine if a binary tree is a valid Binary Search Tree (BST)
def isValidBST(root: Optional[TreeNode]) -> bool:
    # Helper function to validate node values against minimum and maximum constraints
    def valid(node, minimum, maximum):
        # If the current node is None, it is valid
        if not node:
            # Return True
            return True
        
        # Check if the current node's value is within the allowed range
        if not (node.val > minimum and node.val < maximum):
            # If not, return False
            return False
        
        # Recursively validate left and right subtrees with updated constraints
        return valid(node.left, minimum, node.val) and valid(node.right, node.val, maximum)
    
    # Start validation from the root with negative and positive infinity as initial bounds
    return valid(root, float("-inf"), float("inf"))
