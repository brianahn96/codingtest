# Overall Time Complexity: O(N * N!) where N is the length of nums
# Overall Space Complexity: O(N * N!) to store all generated permutations
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

# Define the permute function
def permute(nums: list[int]) -> list[list[int]]:
    """
    Time Complexity: O(N * N!)
    Space Complexity: O(N * N!) to store the result, O(N) for recursion stack.
    """
    # Initialize a list to store all generated permutations
    results = []
    # Initialize a temporary list to record the current permutation being built
    records = []
    
    # Define the DFS helper function
    def dfs(elements):
        """
        Time Complexity: O(N * N!)
        Space Complexity: O(N) for recursion stack.
        """
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
