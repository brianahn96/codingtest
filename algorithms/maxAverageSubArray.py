# Time Complexity: O(N) where N is the length of the array (sliding window)
# Space Complexity: O(1) - Only using constant extra space
#
# https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75

def findMaxAverage(nums: list[int], k: int) -> float:
    curr = max_sum = sum(nums[:k])

    for i in range(k, len(nums)):
        curr += nums[i] - nums[i - k]

        max_sum = max(max_sum, curr)

    return max_sum / k