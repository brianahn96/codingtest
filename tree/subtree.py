# https://leetcode.com/problems/subtree-of-another-tree/description/

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isidentical(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return isidentical(p.left, q.left) and isidentical(p.right, q.right)

        if not root:
            return False

        queue = deque([root])

        while queue:
            node = queue.popleft()

            if isidentical(node, subRoot):
                return True
        
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return False