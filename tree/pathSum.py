# Overall Time Complexity: O(N) for pathSumPrefix, O(N*H) for pathSumPath
# Overall Space Complexity: O(N) for pathSumPrefix, O(H) for pathSumPath

# Source URL for the problem description
# https://leetcode.com/problems/path-sum-iii/description/

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
        
# Import Optional from typing for type hinting
from typing import Optional
# Import defaultdict from collections to store prefix sums
from collections import defaultdict

# Implementation using prefix sum (Time: O(N), Space: O(N))
def pathSumPrefix(root: Optional[TreeNode], targetSum: int) -> int:
    # Initialize a map to store the frequency of prefix sums
    prefix_count = defaultdict(int)
    # Set the initial prefix sum of 0 with frequency 1
    prefix_count[0] = 1

    # Define a DFS function to traverse the tree
    def dfs(node, curr_sum):
        # Check if the current node is None
        if not node:
            # Return 0 for a null node
            return 0

        # Add the current node's value to the running sum
        curr_sum += node.val

        # Find how many previous prefix sums satisfy (curr_sum - prefix_sum = targetSum)
        count = prefix_count[curr_sum - targetSum]

        # Increment the count for the current prefix sum in the map
        prefix_count[curr_sum] += 1

        # Recursively call DFS on the left child and add result to count
        count += dfs(node.left, curr_sum)
        # Recursively call DFS on the right child and add result to count
        count += dfs(node.right, curr_sum)

        # Backtrack: decrement the count of the current prefix sum after visiting subtrees
        prefix_count[curr_sum] -= 1

        # Return the total count of paths found in this subtree
        return count

    # Start the DFS from the root with an initial sum of 0
    return dfs(root, 0)

# Implementation using path list (Time: O(N*H), Space: O(H))
def pathSumPath(root: Optional[TreeNode], targetSum: int) -> int:
    # Define a DFS function that maintains the current path
    def dfs(node, path):
        # Check if the current node is None
        if not node:
            # Return 0 for a null node
            return 0
        
        # Append the current node's value to the path list
        path.append(node.val)
        # Initialize a temporary sum variable
        temp_sum = 0
        # Initialize a count variable for paths ending at the current node
        count = 0
        # Iterate backwards through the current path to find sub-paths matching targetSum
        for val in reversed(path):
            # Accumulate the value
            temp_sum += val
            # Check if the temporary sum equals the target sum
            if temp_sum == targetSum:
                # Increment the count if a match is found
                count += 1
        
        # Recursively call DFS on the left child and add result to count
        count += dfs(node.left, path)
        # Recursively call DFS on the right child and add result to count
        count += dfs(node.right, path)
        # Backtrack: remove the current node's value from the path list
        path.pop()
        # Return the total count of paths found
        return count
    
    # Start the DFS from the root with an empty path list
    return dfs(root, [])
