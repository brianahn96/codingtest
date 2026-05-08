# Overall Time Complexity: O(N log N) due to array slicing in each recursive call
# Overall Space Complexity: O(N) for the resulting tree and O(log N) for the recursion stack

# Source URL for the problem description
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Import Optional and List from typing for type hinting
from typing import Optional, List

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

# Function to convert a sorted array into a height-balanced BST
def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    # Check if the input list is empty
    if not nums:
        # Return None for an empty list
        return None

    # Find the middle index of the current list
    mid = len(nums) // 2

    # Create a new TreeNode with the middle element (to ensure balance)
    node = TreeNode(nums[mid])
    # Recursively build the left subtree using the left half of the list
    node.left = sortedArrayToBST(nums[:mid])
    # Recursively build the right subtree using the right half of the list
    node.right = sortedArrayToBST(nums[mid + 1:])

    # Return the constructed root node of the BST
    return node
