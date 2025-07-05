# https://www.acmicpc.net/problem/2583

from collections import deque

M, N, K = map(int, input().split())
graph = [[0] * N for _ in range(M)]
result = []

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] += 1
            
def bfs(i, j):
    count = 1
    queue = deque()
    queue.append((i, j))
    diff_x = [-1, 0, 1, 0]
    diff_y = [0, 1, 0, -1]
    while queue:
        y, x = queue.popleft()
        for k in range(4):
            new_y, new_x = y + diff_y[k], x + diff_x[k]
            if (0 <= new_y < M) and (0 <= new_x < N) and graph[new_y][new_x] == 0:
                graph[new_y][new_x] += 1
                queue.append((new_y, new_x))
                count += 1
    return count

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            graph[i][j] = 1
            result.append(bfs(i, j))

print(len(result))
print(*sorted(result))