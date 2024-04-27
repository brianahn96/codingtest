# https://school.programmers.co.kr/learn/courses/30/lessons/258705

def solution(n, tops):
    MOD = 10007
    dp1 = [0] * (n + 1)
    dp2 = [0] * (n + 1)
    dp1[1] = 1
    dp2[1] = 2 + tops[0]
    
    for i in range(2, n + 1):
        if not tops[i - 1]:
            dp2[i] = dp1[i - 1] + 2 * dp2[i - 1]
        else:
            dp2[i] = 2 * dp1[i - 1] + 3 * dp2[i - 1]
            
        dp1[i] = dp1[i - 1] + dp2[i - 1]
        
        dp1[i] %= MOD
        dp2[i] %= MOD
    
    return (dp1[n] + dp2[n]) % MOD