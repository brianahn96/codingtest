# https://leetcode.com/problems/maximum-subarray/description/

def maxSubArray(nums: list[int]) -> int:
    sums = [nums[0]]
    
    for i in range(1, len(nums)):
        sums.append(nums[i] + (sums[i-1] if sums[i-1] > 0 else 0))
 
    return max(sums)

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))
