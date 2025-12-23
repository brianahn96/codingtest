# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import Optional

def longestZigZagRecursive(root: Optional[TreeNode]) -> int:
    max_length = 0

    def dfs(node, is_right, length):
        nonlocal max_length

        if not node:
            return

        max_length = max(max_length, length)

        if is_right:
            dfs(node.right, False, length + 1)
            dfs(node.left, True, 1)
        else:
            dfs(node.left, True, length + 1)
            dfs(node.right, False, 1)
        
    dfs(root, True, 0)
    dfs(root, False, 0)
    return max_length


def longestZigZagStack(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    stack = [(root, 0, 0)]
    max_length = 0
    while stack:
        node, left, right = stack.pop()
        max_length = max(max_length, left, right)
        if node.left:
            stack.append((node.left, right + 1, 0))
        if node.right:
            stack.append((node.right, 0, left + 1))
    return max_length