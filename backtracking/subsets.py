# https://leetcode.com/problems/subsets/description/

from typing import List

def subsets(self, nums: List[int]) -> List[List[int]]:
    """
    Time Complexity: O(2^N * N)
    Space Complexity: O(2^N * N) to store the result, O(N) for recursion stack.
    """
    res = []

    def backtracking(index, path):
        """
        Time Complexity: O(2^N * N)
        Space Complexity: O(N) for recursion stack.
        """
        res.append(path.copy())
        for i in range(index, len(nums)):
            path.append(nums[i])
            backtracking(i + 1, path)
            path.pop()

    backtracking(0, [])

    return res