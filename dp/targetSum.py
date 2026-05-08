# https://leetcode.com/problems/target-sum/description/

from collections import defaultdict

def findTargetSumWays(nums: list[int], target: int) -> int:
    dp = {0: 1}

    for num in nums:
        next_dp = defaultdict(int)
        for current_sum, count in dp.items():
            next_dp[current_sum + num] += count
            next_dp[current_sum - num] += count
        dp = next_dp

    return dp.get(target, 0)