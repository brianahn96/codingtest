# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def maxDepthRecursive(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    return max(maxDepthRecursive(root.left) + 1, maxDepthRecursive(root.right) + 1)

def maxDepthBFS(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    queue = deque([root])
    depth = 0
    
    while queue:
        depth += 1
        for _ in range(len(queue)):
            curroot = queue.popleft()
            if curroot.left:
                queue.append(curroot.left)
            if curroot.right:
                queue.append(curroot.right)
    
    return depth