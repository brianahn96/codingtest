# Overall Time Complexity: O(N * M) where N is the number of nodes in root and M in subRoot
# Overall Space Complexity: O(N + H_M) where H_M is the height of subRoot

# Source URL for the problem description
# https://leetcode.com/problems/subtree-of-another-tree/description/

# Import Optional from typing for type hinting
from typing import Optional
# Import deque from collections for breadth-first search
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

# Define the Solution class to solve the subtree problem
class Solution:
    # Method to determine if subRoot is a subtree of root
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Helper function to check if two trees are identical
        def isidentical(p, q):
            # If both nodes are None, they are identical
            if not p and not q:
                # Return True
                return True
            # If one node is None but the other is not
            if not p or not q:
                # Return False
                return False
            # If the values of the two nodes are different
            if p.val != q.val:
                # Return False
                return False
            # Recursively check if left subtrees and right subtrees are identical
            return isidentical(p.left, q.left) and isidentical(p.right, q.right)

        # If the root tree is empty
        if not root:
            # Return False as an empty tree cannot contain a non-empty subRoot
            return False

        # Initialize a queue for BFS traversal of the main tree
        queue = deque([root])

        # Traverse the main tree
        while queue:
            # Dequeue the next node from the main tree
            node = queue.popleft()

            # Check if the tree rooted at the current node is identical to subRoot
            if isidentical(node, subRoot):
                # If a match is found, return True
                return True
        
            # If a left child exists
            if node.left:
                # Enqueue the left child for future checks
                queue.append(node.left)
            # If a right child exists
            if node.right:
                # Enqueue the right child for future checks
                queue.append(node.right)
        
        # If no identical subtree was found after traversing the whole tree
        return False
