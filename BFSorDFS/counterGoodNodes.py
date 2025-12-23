# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from collections import deque

def goodNodes(root: TreeNode) -> int:
    count = 0
    queue = deque()
    queue.append((root, root.val))

    while queue:
        node, value = queue.popleft()
        if node.val >= value:
            count += 1
        max_val = max(node.val, value)
        if node.left:
            queue.append((node.left, max_val))
        if node.right:
            queue.append((node.right, max_val))
    return count