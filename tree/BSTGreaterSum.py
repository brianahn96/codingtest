# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/description/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    val: int = 0
    
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            self.bstToGst(root.right)
            root.val += self.val
            self.val = root.val
            self.bstToGst(root.left)
            
        return root