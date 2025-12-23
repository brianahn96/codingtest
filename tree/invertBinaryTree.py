# https://leetcode.com/problems/invert-binary-tree/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None

    root.left, root.right = invertTree(root.right), invertTree(root.left)

    return root

def invertTreeBFS(root: Optional[TreeNode]) -> Optional[TreeNode]:
    from collections import deque
    
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        
        if node:
            node.left, node.right = node.right, node.left
            queue.append(node.left)
            queue.append(node.right)
    
    return root