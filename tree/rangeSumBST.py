# https://leetcode.com/problems/range-sum-of-bst/description/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rangeSumBSTRecursive(root: Optional[TreeNode], low: int, high: int) -> int:
    if not root:
        return 0
    
    sum = root.val if low <= root.val <= high else 0
    sum += rangeSumBSTRecursive(root.left, low, high)
    sum += rangeSumBSTRecursive(root.right, low, high)
    return sum

def rangeSumBSTDFS(root: Optional[TreeNode], low: int, high: int) -> int:
    
    def dfs(node):
        if not node:
            return 0
        
        if node.val < low:
            return dfs(node.right)
        elif node.val > high:
            return dfs(node.left)
        return node.val + dfs(node.left) + dfs(node.right)
    
    return dfs(root)

def rangeSumBSTDFSSum(root: Optional[TreeNode], low: int, high: int) -> int:
    stack, sum = [root], 0
    
    while stack:
        node = stack.pop()
        if node:
            if node.val > low:
                stack.append(node.left)
            if node.val < high:
                stack.append(node.right)
            if low <= node.val <= high:
                sum += node.val
    return sum