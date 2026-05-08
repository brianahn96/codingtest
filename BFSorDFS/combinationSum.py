# Overall Time Complexity: O(N^((T/M)+1)) where N is the number of candidates, T is target, M is min candidate value
# Overall Space Complexity: O(T/M) for recursion stack depth
# https://leetcode.com/problems/combination-sum/description/

# Given an array of distinct integers candidates and a target integer target, 
# return a list of all unique combinations of candidates where the chosen numbers sum to target. 
# You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. 
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.

# These are the only two combinations.

# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]

# Example 3:

# Input: candidates = [2], target = 1
# Output: []

# Import List for type hinting
from typing import List

# Define the combinationSum function
def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    # Initialize the list to store valid combinations
    results = []
    
    # Define the depth-first search helper function
    def dfs(cumul, index, path):
        
        # Check if the cumulative sum has dropped below zero
        if cumul < 0:
            # If negative, this path is invalid, so return
            return
        
        # Check if the target cumulative sum has been reached
        if cumul == 0:
            # Append a copy of the valid path to results
            results.append(path)
            # Return to continue searching other paths
            return
        
        # Iterate through candidates starting from the current index to avoid duplicates
        for i in range(index, len(candidates)):
            # Recursively call dfs with reduced sum and updated path
            dfs(cumul - candidates[i], i, path + [candidates[i]])
    
    # Initiate the DFS search with the initial target and an empty path
    dfs(target, 0, [])
    # Return the collected valid combinations
    return results
