# Overall Time Complexity: O(N)
# Overall Space Complexity: O(H) for recursion, O(W) for BFS

# Source URL for the problem description
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Import Optional from typing for type hinting
from typing import Optional
# Import deque from the collections module for efficient queue operations
from collections import deque

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
        
# Recursive function to calculate the maximum depth of a binary tree
def maxDepthRecursive(root: Optional[TreeNode]) -> int:
    # Check if the current node is None
    if not root:
        # Return 0 for an empty tree/leaf child
        return 0
    
    # Return 1 plus the maximum depth of the left or right subtrees
    return max(maxDepthRecursive(root.left) + 1, maxDepthRecursive(root.right) + 1)

# Iterative function to calculate the maximum depth using BFS
def maxDepthBFS(root: Optional[TreeNode]) -> int:
    # Check if the root node is None
    if not root:
        # Return 0 for an empty tree
        return 0
    
    # Initialize a queue for level-order traversal with the root node
    queue = deque([root])
    # Initialize the depth counter as 0
    depth = 0
    
    # Process nodes level by level
    while queue:
        # Increment the depth for each level reached
        depth += 1
        # Iterate over all nodes at the current level
        for _ in range(len(queue)):
            # Dequeue the next node
            current = queue.popleft()
            # If the current node has a left child
            if current.left:
                # Enqueue the left child for the next level
                queue.append(current.left)
            # If the current node has a right child
            if current.right:
                # Enqueue the right child for the next level
                queue.append(current.right)
    
    # Return the final maximum depth
    return depth
