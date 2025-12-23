# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import Optional
from collections import deque

def maxLevelSum(root: Optional[TreeNode]) -> int:
    depth = 1
    max_level = 1
    max_sum = float("-inf")
    queue = deque([root])

    while queue:
        summed = 0
        for _ in range(len(queue)):
            node = queue.popleft()
            summed += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if summed > max_sum:
            max_sum = summed
            max_level = depth 
        depth += 1
    
    return max_level