# Overall Time Complexity: O(N)
# Overall Space Complexity: O(H) where H is the tree height

# Source URL for the problem description
# https://leetcode.com/problems/balanced-binary-tree/description/

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

# Function to determine if a binary tree is height-balanced
def isBalanced(root: Optional[TreeNode]) -> bool:
    # Helper function to check balance and return height
    def check(node):
        # Check if the current node is None
        if not node:
            # Return 0 as the height of a null node
            return 0

        # Recursively check the left subtree and get its height
        left = check(node.left)
        # Recursively check the right subtree and get its height
        right = check(node.right)

        # If any subtree is unbalanced or current height difference > 1
        if left == -1 or right == -1 or abs(left - right) > 1:
            # Return -1 to signify that the tree is unbalanced
            return -1
        
        # Return the height of the current node
        return max(left, right) + 1

    # Return True if the check function does not return -1
    return check(root) != -1
