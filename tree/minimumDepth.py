# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(root: Optional[TreeNode]) -> int:
    from collections import deque

    if not root:
        return 0

    depth = 1
    queue = deque([(root, depth)])

    while queue:
        node, depth = queue.popleft()
        if not node.left and not node.right:
            return depth

        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))