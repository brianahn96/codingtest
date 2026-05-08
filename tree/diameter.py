# Overall Time Complexity: O(N)
# Overall Space Complexity: O(H) where H is the tree height

# Source URL for the problem description
# https://leetcode.com/problems/diameter-of-binary-tree/description/

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
 
# Define the Solution class to solve the diameter problem
class Solution:
    # Initialize a class-level variable to store the longest path found
    longest = 0

    # Method to calculate the diameter of a binary tree
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # Define a DFS helper function to find the maximum depth of each node
        def dfs(node):
            # Check if the current node is None
            if not node:
                # Return 0 for an empty node's depth
                return 0
            
            # Recursively find the depth of the left subtree
            left = dfs(node.left)
            # Recursively find the depth of the right subtree
            right = dfs(node.right)

            # Update the longest path by comparing it with the sum of left and right depths
            self.longest = max(self.longest, left + right)

            # Return the maximum depth of the current node to its parent
            return max(left, right) + 1
		
        # Start the DFS from the root node
        dfs(root)
        # Return the final longest path (diameter) found
        return self.longest
