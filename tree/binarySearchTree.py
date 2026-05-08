# Overall Time Complexity: O(H) where H is the tree height
# Overall Space Complexity: O(H) where H is the tree height

# Source URL for the problem description
# https://leetcode.com/problems/search-in-a-binary-search-tree/description/

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

# Function to search for a value in a BST using an explicit stack (Iterative)
def searchBSTStack(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    # Initialize a stack with the root node
    stack = [root]

    # Process nodes as long as the stack is not empty
    while stack:
        # Pop the top node from the stack
        node = stack.pop()

        # Check if the current node is None
        if not node:
            # Skip to the next iteration
            continue

        # If the current node's value matches the target value
        if node.val == val:
            # Return the current node
            return node
        # If the current node's value is less than the target
        elif node.val < val:
            # Push the right child onto the stack (search right)
            stack.append(node.right)
        # If the current node's value is greater than the target
        else:
            # Push the left child onto the stack (search left)
            stack.append(node.left)

    # Return None (implicitly via return) if the value is not found
    return

# Function to search for a value in a BST using recursion
def searchBSTRecursive(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    # Check if the current node is None
    if not root:
        # Return None as the value cannot be found
        return None
    
    # Check if the current node's value matches the target value
    if root.val == val:
        # Return the current node
        return root
    # If the current node's value is greater than the target
    elif root.val > val:
        # Recursively search in the left subtree
        return searchBSTRecursive(root.left, val)
    # If the current node's value is less than the target
    else:
        # Recursively search in the right subtree
        return searchBSTRecursive(root.right, val)
