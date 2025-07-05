# https://leetcode.com/problems/diameter-of-binary-tree/description/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 
class Solution:
    longest = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            self.longest = max(self.longest, left + right)

            return max(left, right) + 1
		
        dfs(root)
        return self.longest
        