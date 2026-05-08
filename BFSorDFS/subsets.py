# Overall Time Complexity: O(N * 2^N) where N is number of elements in nums
# Overall Space Complexity: O(N * 2^N) to store all the generated subsets
# Given an integer array nums of unique elements, return all possible 
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.


# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:

# Input: nums = [0]
# Output: [[],[0]]

# Define the subsets function
def subsets(nums: list[int]) -> list[list[int]]:
    # Initialize a list to store all generated subsets
    results = []
    
    # Define the DFS helper function
    def dfs(index, path):
        # Add the current path (a valid subset) to results
        results.append(path)
        
        # Iterate through the elements starting from the current index
        for i in range(index, len(nums)):
            # Recurse with the next index and updated path including the current element
            dfs(i + 1, path + [nums[i]])
    
    # Start the DFS search with index 0 and an empty subset
    dfs(0, [])
    
    # Return the final list of all subsets
    return results
