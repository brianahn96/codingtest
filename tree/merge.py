# Overall Time Complexity: O(N)
# Overall Space Complexity: O(H) where H is the tree height

# Source URL for the problem description
# https://leetcode.com/problems/merge-two-binary-trees/description/

# Import Optional from the typing module for type hinting
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
        
# Define the Solution class to solve the merging problem
class Solution:
    # Method to merge two binary trees into one
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # Check if both current nodes exist in root1 and root2
        if root1 and root2:
            # Create a new node with the sum of the values from both trees
            node = TreeNode(root1.val + root2.val)
            # Recursively merge the left children of both nodes
            node.left = self.mergeTrees(root1.left, root2.left)
            # Recursively merge the right children of both nodes
            node.right = self.mergeTrees(root1.right, root2.right)

            # Return the newly created merged node
            return node
        # Handle cases where one or both nodes are None
        else:
            # If root1 exists but root2 does not
            if root1 and not root2:
                # Return root1 as the merged branch
                return root1
            # If root2 exists but root1 does not
            elif not root1 and root2:
                # Return root2 as the merged branch
                return root2
            # If both nodes are None
            else:
                # Return None as there is nothing to merge
                return None
