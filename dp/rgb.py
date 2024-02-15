# https://www.acmicpc.net/problem/1149

N = int(input())
grids = [0] * N
for i in range(N):
    grids[i] = list(map(int, input().split(" ")))
    
for i in range(1, N):
    grids[i][0] = min(grids[i - 1][1], grids[i - 1][2]) + grids[i][0]
    grids[i][1] = min(grids[i - 1][0], grids[i - 1][2]) + grids[i][1]
    grids[i][2] = min(grids[i - 1][0], grids[i - 1][1]) + grids[i][2]
    
print(min(grids[N - 1]))