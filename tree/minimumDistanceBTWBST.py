# Overall Time Complexity: O(N)
# Overall Space Complexity: O(H) where H is the tree height

# Source URL for the problem description
# https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/

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
        
# Define the Solution class to solve the minimum difference problem in BST
class Solution:
    # Initialize a class-level variable for the minimum difference
    result = float('inf')
    # Initialize a class-level variable for the previously visited node's value
    prev = -1 * float('inf')
    
    # Method to calculate the minimum difference between any two nodes
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # If a left child exists, visit it (in-order traversal)
        if root.left:
            # Recursively call minDiffInBST on the left child
            self.minDiffInBST(root.left)
        
        # Calculate the difference between current value and previous value and update result
        self.result = min(self.result, root.val - self.prev)
        # Update the previous value to the current node's value
        self.prev = root.val

        # If a right child exists, visit it
        if root.right:
            # Recursively call minDiffInBST on the right child
            self.minDiffInBST(root.right)

        # Return the final minimum difference found
        return self.result

# Define a second Solution class using an iterative approach
class Solution2:
    # Method to calculate the minimum difference iteratively
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # Initialize the minimum difference
        result = float('inf')
        # Initialize the previously visited value
        prev = -1 * float('inf')

        # Initialize an empty stack for in-order traversal
        stack = []
        # Start with the root node
        node = root
        # Continue as long as there are nodes to process or stack is not empty
        while stack or node:
            # Traverse to the leftmost node
            while node:
                # Push the current node onto the stack
                stack.append(node)
                # Move to the left child
                node = node.left
            
            # Pop the most recent node from the stack
            node = stack.pop()

            # Update the result with the minimum difference
            result = min(result, node.val - prev)
            # Update the previous value
            prev = node.val

            # Move to the right child
            node = node.right
        
        # Return the final minimum difference
        return result
            
# Helper function to build a tree from preorder and inorder traversals
def buildTree(preorder, inorder):
    # Check if the inorder list is not empty
    if inorder:
        # Find the index of the root in the inorder list
        index = inorder.index(preorder.pop(0))
        # Create a new TreeNode with the found value
        node = TreeNode(inorder[index])
        # Recursively build the left subtree
        node.left = buildTree(preorder, inorder[0:index])
        # Recursively build the right subtree
        node.right = buildTree(preorder, inorder[index + 1:])
        # Return the constructed node
        return node
