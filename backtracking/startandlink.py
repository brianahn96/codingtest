# https://www.acmicpc.net/problem/14889

N = int(input())
grids = [0 for _ in range(N)]
for i in range(N):
    lists = list(map(int, input().split(" ")))
    grids[i] = lists
    
minimum = int(1e9)
visited = [False for _ in range(N)]

def backtracking(depth, index):
    global minimum
    if depth == N // 2:
        power1, power2 = 0, 0
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if visited[i] and visited[j]:
                    power1 += grids[i][j]
                elif not visited[i] and not visited[j]:
                    power2 += grids[i][j]
        minimum = min(minimum, abs(power1-power2)) 
        return
    
    for i in range(index, N):
        visited[i] = True
        backtracking(depth + 1, i + 1)
        visited[i] = False
        
backtracking(0, 0)

print(minimum)