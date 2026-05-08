# https://www.acmicpc.net/problem/9663

N = int(input())
answer = 0
grids = [0] * N

def check(x):
    """
    Time Complexity: O(x) which is O(N) in worst case.
    Space Complexity: O(1)
    """
    for i in range(x):
        if grids[x] == grids[i]:
            return False
        if abs(grids[x] - grids[i]) == abs(x - i):
            return False
    return True

def nqueen(n):
    """
    Time Complexity: O(N!)
    Space Complexity: O(N) for recursion stack and grids array.
    """
    global answer
    if n == N:
        answer += 1
        return
    for i in range(N):
        grids[n] = i
        if check(n):
            nqueen(n + 1)

nqueen(0)