# Overall Time Complexity: O(N)
# Overall Space Complexity: O(W) where W is the maximum width of the tree

# Source URL for the problem description
# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/

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
# Import deque from the collections module for efficient queue operations
from collections import deque

# Function to find the level with the maximum sum in a binary tree
def maxLevelSum(root: Optional[TreeNode]) -> int:
    # Initialize the current depth as 1
    depth = 1
    # Initialize the level with the maximum sum as 1
    max_level = 1
    # Initialize the maximum sum with negative infinity
    max_sum = float("-inf")
    # Initialize a queue for BFS with the root node
    queue = deque([root])

    # Process nodes level by level
    while queue:
        # Initialize a variable to store the sum of values at the current level
        summed = 0
        # Iterate over the number of nodes at the current level
        for _ in range(len(queue)):
            # Dequeue the next node
            node = queue.popleft()
            # Add the node's value to the current level's sum
            summed += node.val
            # If a left child exists
            if node.left:
                # Enqueue the left child for the next level
                queue.append(node.left)
            # If a right child exists
            if node.right:
                # Enqueue the right child for the next level
                queue.append(node.right)
        # Check if the current level's sum is greater than the maximum sum found so far
        if summed > max_sum:
            # Update the maximum sum
            max_sum = summed
            # Update the level index of the maximum sum
            max_level = depth 
        # Increment the depth for the next level
        depth += 1
    
    # Return the level index that had the maximum sum
    return max_level
