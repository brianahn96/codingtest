
# https://www.acmicpc.net/problem/2178

from collections import deque

M, N = map(int, input().split())
graph = []

for i in range(M):
    graph.append(list(map(int,input())))

def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    diff_x = [-1, 0, 1, 0]
    diff_y = [0, 1, 0, -1]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            new_x, new_y = x + diff_x[i], y + diff_y[i]
            
            if 0 <= new_x < M and 0 <= new_y < N and graph[new_x][new_y] == 1:
                graph[new_x][new_y] = graph[x][y] + 1
                queue.append((new_x, new_y))
    
    return graph[M - 1][N - 1]

print(bfs(0,0))