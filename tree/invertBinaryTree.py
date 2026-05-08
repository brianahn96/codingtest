# Overall Time Complexity: O(N)
# Overall Space Complexity: O(H) for recursion, O(W) for BFS

# Source URL for the problem description
# https://leetcode.com/problems/invert-binary-tree/

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

# Recursive function to invert a binary tree
def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    # Check if the current node is None
    if not root:
        # Return None for an empty node
        return None

    # Swap the left and right children and recursively invert them
    root.left, root.right = invertTree(root.right), invertTree(root.left)

    # Return the current root after inversion
    return root

# Iterative function to invert a binary tree using Breadth-First Search
def invertTreeBFS(root: Optional[TreeNode]) -> Optional[TreeNode]:
    # Import deque from the collections module for efficient queue operations
    from collections import deque
    
    # Initialize a queue for BFS with the root node
    queue = deque([root])
    
    # Process nodes as long as the queue is not empty
    while queue:
        # Dequeue the next node
        node = queue.popleft()
        
        # Check if the current node is not None
        if node:
            # Swap the left and right children of the current node
            node.left, node.right = node.right, node.left
            # Enqueue the left child for future processing
            queue.append(node.left)
            # Enqueue the right child for future processing
            queue.append(node.right)
    
    # Return the original root after the entire tree is inverted
    return root
