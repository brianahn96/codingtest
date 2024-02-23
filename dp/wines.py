# https://www.acmicpc.net/problem/2156

N = int(input())
wines = [0] * (N + 1)
for i in range(1, N + 1):
    wines[i] = int(input())
    
dp = [0] * (N + 1)
dp[1] = wines[1]
if N > 1:
    dp[2] = wines[1] + wines[2]

for i in range(3, N + 1):
    dp[i] = max(dp[i - 1],dp[i - 3] + wines[i - 1] + wines[i], dp[i - 2] + wines[i])
    
print(dp[N])