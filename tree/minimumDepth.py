# Overall Time Complexity: O(N)
# Overall Space Complexity: O(W) where W is the maximum width of the tree

# Source URL for the problem description
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

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

# Function to find the minimum depth of a binary tree
def minDepth(root: Optional[TreeNode]) -> int:
    # Import deque from the collections module for efficient queue operations
    from collections import deque

    # Check if the root node is None
    if not root:
        # Return 0 as the depth of an empty tree
        return 0

    # Initialize the depth as 1 for the root node
    depth = 1
    # Initialize a queue for level-order traversal (BFS) with the root and its depth
    queue = deque([(root, depth)])

    # Continue traversal as long as the queue is not empty
    while queue:
        # Dequeue the next node and its corresponding depth
        node, depth = queue.popleft()
        # Check if the current node is a leaf (no children)
        if not node.left and not node.right:
            # Return the depth as soon as the first leaf is reached (guaranteed minimum depth)
            return depth

        # If a left child exists
        if node.left:
            # Enqueue the left child with an incremented depth
            queue.append((node.left, depth + 1))
        # If a right child exists
        if node.right:
            # Enqueue the right child with an incremented depth
            queue.append((node.right, depth + 1))
