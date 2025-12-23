# https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75


def moveZeroes(nums: list[int]) -> None:
    index = 0

    while index < len(nums):
        if nums[index] == 0 and index < len(nums) - 1:
            right = index
            while right < len(nums) and nums[right] == 0:
                right += 1
            if right < len(nums):
                nums[index], nums[right] = nums[right], nums[index]
        index += 1

def moveZeroesOptimized(nums: list[int]) -> None:
    n = len(nums)
    start = 0
    for i in range(n):
        if nums[i] != 0:
            nums[i],nums[start] = nums[start],nums[i]
            start += 1