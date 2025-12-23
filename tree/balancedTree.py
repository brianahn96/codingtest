# https://leetcode.com/problems/balanced-binary-tree/description/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root: Optional[TreeNode]) -> bool:
    def check(node):
        if not node:
            return 0

        left = check(node.left)
        right = check(node.right)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        
        return max(left, right) + 1

    return check(root) != -1