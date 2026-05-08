# https://leetcode.com/problems/climbing-stairs/description/

from collections import defaultdict

def climbStairs(n: int) -> int:
    dp = defaultdict(int)
    
    def climb(n):
        if n <= 2:
            return n
        
        if dp[n]:
            return dp[n]
        
        dp[n] = climb(n - 1) + climb(n - 2)
        
        return dp[n]
    
    return climb(n)

n = 3
print(climbStairs(n))
