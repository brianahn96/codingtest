# Overall Time Complexity: O(N)
# Overall Space Complexity: O(H) where H is the tree height

# Source URL for the problem description
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

# Define the TreeNode class representing a node in a binary tree
class TreeNode:
    # Initialize a new TreeNode with a given value
    def __init__(self, x):
        # Assign the value to the node
        self.val = x
        # Initialize the left child as None
        self.left = None
        # Initialize the right child as None
        self.right = None

# Import Optional from the typing module for type hinting
from typing import Optional

# Function to find the lowest common ancestor of two nodes p and q
def lowestCommonAncestor(root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
    # Check if the current node is None or matches either p or q
    if not root or root == p or root == q:
        # Return the current root if it's None, p, or q
        return root

    # Recursively find the common ancestor in the left subtree
    left = lowestCommonAncestor(root.left, p, q)
    # Recursively find the common ancestor in the right subtree
    right = lowestCommonAncestor(root.right, p, q)

    # If both left and right are not None, the current node is the ancestor
    if left and right:
        # Return the current root as the lowest common ancestor
        return root

    # If only the left subtree returned a node, return that node
    if left: return left
    # If only the right subtree returned a node, return that node
    if right: return right
