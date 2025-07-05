# https://www.acmicpc.net/problem/15652

N, M = map(int, input().split())

s = []

def backtracking(index):
    if len(s) == M:
        print(" ".join(map(str, s)))
        return
    for i in range(index, N + 1):
        s.append(i)
        backtracking(i)
        s.pop()

backtracking(1)