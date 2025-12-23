# https://leetcode.com/problems/max-consecutive-ones-iii/description/?envType=study-plan-v2&envId=leetcode-75

def longestOnes(nums: list[int], k: int) -> int:
    left, maxLength, zeroCount = 0, 0, 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zeroCount += 1
            while zeroCount > k:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1
            maxLength = max(maxLength, right - left + 1)
    return maxLength
    
def longestOnesOptimized(nums: list[int], k: int) -> int:
    left = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            k -= 1
            
        if k < 0:
            if nums[left] == 0:
                k += 1
            left += 1
    
    return right - left + 1