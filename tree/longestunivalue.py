# https://leetcode.com/problems/longest-univalue-path/description/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    ans = 0
    
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0
            
            self.ans = max(self.ans, left + right)
            return max(left, right)
        
        dfs(root)
        return self.ans