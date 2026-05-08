# Time Complexity: O(N) where N is the length of the array (sliding window)
# Space Complexity: O(1) - Only using constant extra space
#
# https://leetcode.com/problems/minimum-size-subarray-sum/description/

def minSubArrayLen(target: int, nums: list[int]) -> int:
    minlen = float('inf')
    l = 0
    sum = 0
    for r in range(len(nums)):
        sum += nums[r]
        while sum >= target:
            minlen = min(minlen, r-l+1)
            sum -= nums[l]
            l += 1
    return minlen if minlen != float("inf") else 0