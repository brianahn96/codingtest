# https://www.acmicpc.net/problem/15652

N, M = map(int, input().split())

s = []

def backtracking(index):
    """
    Time Complexity: O(H(N, M) * M) where H(N, M) = C(N+M-1, M)
    Space Complexity: O(M) for the recursion stack and state list.
    """
    if len(s) == M:
        print(" ".join(map(str, s)))
        return
    for i in range(index, N + 1):
        s.append(i)
        backtracking(i)
        s.pop()

backtracking(1)