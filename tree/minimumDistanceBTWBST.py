# https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    result = float('inf')
    prev = -1 * float('inf')
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root.left:
            self.minDiffInBST(root.left)
        
        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val

        if root.right:
            self.minDiffInBST(root.right)

        return self.result

class Solution2:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        result = float('inf')
        prev = -1 * float('inf')

        stack = []
        node = root
        while stack and node:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()

            result = min(result, node.val - prev)
            prev = node.val

            node = node.right
            
def buildTree(preorder, inorder):
    if inorder:
        index = inorder.index(preorder.pop(0))
        node = TreeNode(inorder[index])
        node.left = buildTree(preorder, inorder[0:index])
        node.right = buildTree(preorder, inorder[index + 1:])
        return node