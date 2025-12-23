# https://leetcode.com/problems/path-sum-iii/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import Optional
from collections import defaultdict

def pathSumPrefix(root: Optional[TreeNode], targetSum: int) -> int:
    prefix_count = defaultdict(int)
    prefix_count[0] = 1

    def dfs(node, curr_sum):
        if not node:
            return 0

        curr_sum += node.val

        count = prefix_count[curr_sum - targetSum]

        prefix_count[curr_sum] += 1

        count += dfs(node.left, curr_sum)
        count += dfs(node.right, curr_sum)

        prefix_count[curr_sum] -= 1

        return count

    return dfs(root, 0)

def pathSumPath(root: Optional[TreeNode], targetSum: int) -> int:
    def dfs(node, path):
        if not node:
            return 0
        
        path.append(node.val)
        temp_sum = 0
        count = 0
        for val in reversed(path):
            temp_sum += val
            if temp_sum == targetSum:
                count += 1
        
        count += dfs(node.left, path)
        count += dfs(node.right, path)
        path.pop()
        return count
    
    return dfs(root, [])