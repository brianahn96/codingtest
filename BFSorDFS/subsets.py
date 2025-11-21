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

def subsets(nums: list[int]) -> list[list[int]]:
    results = []
    
    def dfs(index, path):
        results.append(path)
        
        for i in range(index, len(nums)):
            dfs(i + 1, path + [nums[i]])
    
    dfs(0, [])
    
    return results