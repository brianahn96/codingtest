# https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75

def moveZeroes(nums: list[int]) -> None:
    insert = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insert] = nums[i]
            insert += 1

    for i in range(insert, len(nums)):
        nums[i] = 0

def moveZeroesOptimized(nums: list[int]) -> None:
    n = len(nums)
    start = 0
    for i in range(n):
        if nums[i] != 0:
            nums[i],nums[start] = nums[start],nums[i]
            start += 1