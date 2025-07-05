# https://www.acmicpc.net/problem/1389

from collections import deque

N, M = map(int, input().split())

network = [[] for _ in range(N + 1)]

results = []

for i in range(M):
    j, k = map(int, input().split())
    network[j].append(k)
    network[k].append(j)

def bfs(i):
    visited = [-1] * (N + 1)

    queue = deque()
    queue.append(i)
    visited[i] = 0

    while queue:
        node = queue.popleft()

        for next_node in network[node]:
            if visited[next_node] == -1:
                visited[next_node] = visited[node] + 1
                queue.append(next_node)

    total = sum(visited) + 1
    return (i, total)

for i in range(1, N + 1):
    results.append(bfs(i))

print(min(results, key = lambda x: x[1])[0])