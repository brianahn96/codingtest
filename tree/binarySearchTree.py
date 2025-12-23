# https://leetcode.com/problems/search-in-a-binary-search-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

def searchBSTStack(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    stack = [root]

    while stack:
        node = stack.pop()

        if not node:
            continue

        if node.val == val:
            return node
        elif node.val < val:
            stack.append(node.right)
        else:
            stack.append(node.left)

    return

def searchBSTRecursive(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return None
    
    if root.val == val:
        return root
    elif root.val > val:
        return searchBSTRecursive(root.left, val)
    else:
        return searchBSTRecursive(root.right, val)