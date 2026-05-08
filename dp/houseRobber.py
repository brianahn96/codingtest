# https://leetcode.com/problems/house-robber/description/

def rob(nums: list[int]) -> int:
    
    def _rob(i):
        if i < 0:
            return 0
        return max(nums[i] + _rob(i - 2), _rob(i - 1))
    
    return _rob(len(nums) - 1)
    
def robdp(nums: list[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    dp = [0] * len(nums)
    
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
    return dp[-1]
    
nums = [1,2,3,1]
print(rob(nums))
print(robdp(nums))
