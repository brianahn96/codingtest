# https://leetcode.com/problems/product-of-array-except-self/description/

from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    p = 1
    res = []

    for num in nums:
        res.append(p)
        p *= num
    
    p = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] = res[i] * p
        p *= nums[i]

    return res