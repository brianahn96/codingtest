# https://leetcode.com/problems/binary-tree-right-side-view/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import Optional
from collections import deque

def rightSideView(root: Optional[TreeNode]) -> list[int]:
    if not root: return []
    res = []
    queue = deque([root])

    while queue:
        for i in range(len(queue)):
            node = queue.popleft()
            if i == 0:
                res.append(node.val)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)

    return res