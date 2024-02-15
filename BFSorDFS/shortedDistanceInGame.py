# https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque

def solution(maps):
    M, N = len(maps), len(maps[0])
    queue = deque()
    queue.append((0,0))
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]
            if 0 <= new_x < M and 0 <= new_y < N and maps[new_x][new_y] == 1:
                queue.append((new_x, new_y))
                maps[new_x][new_y] = maps[x][y] + 1
        
    answer = maps[M - 1][N - 1]
    
    return answer if answer != 1 else -1