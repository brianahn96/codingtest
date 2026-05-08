# Overall Time Complexity: O(N)
# Overall Space Complexity: O(N)

# Source URL for the problem description
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

# Define the TreeNode class representing a node in a binary tree
class TreeNode:
    # Initialize a new TreeNode with value, left child, and right child
    def __init__(self, val=0, left=None, right=None):
        # Assign the value to the node
        self.val = val
        # Assign the left child to the node
        self.left = left
        # Assign the right child to the node
        self.right = right

# Import deque from the collections module for efficient queue operations
from collections import deque

# Define the Codec class to handle serialization and deserialization
class Codec:
    # Method to convert a tree into a list of strings
    def serialize(self, root: TreeNode) -> list[str]:
        # Initialize a queue for level-order traversal starting with the root
        queue = deque([root])
        # Initialize the result list with a placeholder if needed (though logic starts empty)
        result = []
        
        # Traverse the tree using BFS
        while queue:
            # Dequeue the next node
            node = queue.popleft()
            # Check if the node is not None
            if node:
                # Append the node's value as a string to the result
                result.append(str(node.val))
                # Enqueue the left child (even if None)
                queue.append(node.left)
                # Enqueue the right child (even if None)
                queue.append(node.right)
            # If the node is None
            else:
                # Append "null" to the result to represent a missing node
                result.append("null")
                
        # Return the serialized list of strings
        return result
    
    # Method to convert serialized data back into a tree
    def deserialize(self, data: list[str]) -> TreeNode:
        # Check if the data represents an empty tree or starts with "null"
        if not data or data[0] == "null": return None
        
        # The data is already a list of strings in this implementation
        nodes = data
        
        # Create the root node from the first element
        root = TreeNode(int(nodes[0]))
        
        # Initialize a queue for reconstruction starting with the root
        queue = deque([root])
        
        # Initialize an index to track the children in the nodes list
        i = 1
        
        # Reconstruct the tree using BFS
        while queue:
            # Dequeue the current parent node
            curr = queue.popleft()
            # Check if the next element in the list is not "null" (left child)
            if i < len(nodes) and nodes[i] != "null":
                # Create the left child node
                curr.left = TreeNode(int(nodes[i]))
                # Enqueue the left child for future processing
                queue.append(curr.left)
            # Increment index to move to the next element
            i += 1
            # Check if the next element in the list is not "null" (right child)
            if i < len(nodes) and nodes[i] != "null":
                # Create the right child node
                curr.right = TreeNode(int(nodes[i]))
                # Enqueue the right child for future processing
                queue.append(curr.right)
            # Increment index to move to the next element
            i += 1
            
        # Return the reconstructed root node
        return root
