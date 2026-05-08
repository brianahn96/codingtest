# Overall Time Complexity: O(N)
# Overall Space Complexity: O(H) where H is the tree height

# Source URL for the problem description
# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/description/

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
        
# Define the Solution class to solve the BST to GST conversion
class Solution:
    # Initialize a class-level variable to keep track of the cumulative sum
    val: int = 0
    
    # Method to convert a BST to a Greater Sum Tree (GST)
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Check if the current node exists
        if root:
            # Recursively visit the right subtree (contains larger values)
            self.bstToGst(root.right)
            # Update the current node's value with the cumulative sum
            root.val += self.val
            # Update the cumulative sum with the new value of the current node
            self.val = root.val
            # Recursively visit the left subtree (contains smaller values)
            self.bstToGst(root.left)
            
        # Return the modified root node
        return root
