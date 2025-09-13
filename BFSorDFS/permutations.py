# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.


# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

# Example 3:

# Input: nums = [1]
# Output: [[1]]

def permute(nums: list[int]) -> list[list[int]]:
    results = []
    records = []
    
    def dfs(elements):
        if len(elements) == 0:
            results.append(records[:])
            
        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            records.append(e)
            dfs(next_elements)
            records.pop()

    dfs(nums)
    return results