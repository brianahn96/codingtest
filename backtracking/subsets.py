# https://leetcode.com/problems/subsets/description/

from typing import List

def subsets(self, nums: List[int]) -> List[List[int]]:
    res = []

    def backtracking(index, path):
        res.append(path.copy())
        for i in range(index, len(nums)):
            path.append(nums[i])
            backtracking(i + 1, path)
            path.pop()

    backtracking(0, [])

    return res