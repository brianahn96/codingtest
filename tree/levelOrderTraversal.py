# https://www.geeksforgeeks.org/problems/level-order-traversal/1

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def levelOrder(root):
    from collections import deque
    res = []
    queue = deque([root])
    
    while queue:
        values = []
        for _ in range(len(queue)):
            node = queue.popleft()
            values.append(node.data)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(values)
        
    return res