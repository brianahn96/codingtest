from collections import defaultdict

class Solution:
    memoization_dp = defaultdict(int)
    tabulation_dp = defaultdict(int)
    
    def fib_memoization(self, N: int) -> int:
        if N <= 1:
            return N
        
        if self.memoization_dp[N]:
            return self.memoization_dp[N]
        
        self.memoization_dp[N] = self.fib_memoization(N-1) + self.fib_memoization(N-2)
        return self.memoization_dp[N]
    
    def fib_tabulation(self, N: int) -> int: 
        self.tabulation_dp[1] = 1
        
        for i in range(2, N+1):
            self.tabulation_dp[i] = self.tabulation_dp[i-1] + self.tabulation_dp[i-2]
        
        return self.tabulation_dp[N]
