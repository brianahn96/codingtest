# https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=study-plan-v2&envId=leetcode-75

def maxOperations(nums: list[int], k: int) -> int:
    nums.sort()
    res = 0
    left, right = 0, len(nums) - 1

    while left < right:
        comp = k - nums[left]
        if nums[right] == comp:
            res += 1
            left +=1
            right -= 1
        elif nums[right] > comp:
            right -= 1
        else:
            left += 1
    return res