# Overall Time Complexity: O(N)
# Overall Space Complexity: O(H) where H is the tree height

# Source URL for the problem description
# https://leetcode.com/problems/longest-univalue-path/description/

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
        
# Define the Solution class to solve the problem
class Solution:
    # Initialize the maximum univalue path length as 0
    ans = 0
    
    # Method to calculate the longest univalue path in the tree
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        # Helper function for depth-first search
        def dfs(node):
            # Check if the current node is None
            if not node:
                # Return 0 for a null node
                return 0

            # Recursively find the longest path in the left child
            left = dfs(node.left)
            # Recursively find the longest path in the right child
            right = dfs(node.right)

            # Check if the left child exists and has the same value as the current node
            if node.left and node.left.val == node.val:
                # Increment the left path length by 1
                left += 1
            # Otherwise, the path does not continue from the left child
            else:
                # Reset the left path length to 0
                left = 0
            
            # Check if the right child exists and has the same value as the current node
            if node.right and node.right.val == node.val:
                # Increment the right path length by 1
                right += 1
            # Otherwise, the path does not continue from the right child
            else:
                # Reset the right path length to 0
                right = 0
            
            # Update the global maximum path length with the sum of left and right paths
            self.ans = max(self.ans, left + right)
            # Return the maximum single-side path length to the parent
            return max(left, right)
        
        # Start the DFS from the root node
        dfs(root)
        # Return the maximum univalue path length found
        return self.ans
