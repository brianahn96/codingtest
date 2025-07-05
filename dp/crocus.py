# https://www.acmicpc.net/problem/9461

N = int(input())

base = [0, 1, 1, 1, 2, 2]

def lists(n):
    dp = [0] * (n + 1)

    if n <= 5:
        print(base[n])
        return
    
    for i in range(1, 6):
        dp[i] = base[i]
    
    for i in range(6, n + 1):
        dp[i] = dp[i - 1] + dp[i - 5]
    
    print(dp[n])

for i in range(N):
    t = int(input())
    lists(t)