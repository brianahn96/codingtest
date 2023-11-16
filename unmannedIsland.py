# https://school.programmers.co.kr/learn/courses/30/lessons/154540

from collections import deque

def solution(maps):
    vertical, horizontal = len(maps), len(maps[0])
    maps = [list(map(str, maps[i])) for i in range(len(maps))]
    dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
    result = []
    
    def bfs(i, j):
        queue = deque()
        queue.append((i, j))
        visited = []
        count = 0
        
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                new_x, new_y = x + dx[i], y + dy[i]
                if 0 <= new_x < vertical and 0 <= new_y < horizontal and (new_x, new_y) not in visited and maps[new_x][new_y] != 'X':
                    queue.append((new_x, new_y))
                    visited.append((new_x, new_y))

            count += int(maps[x][y])
            maps[x][y] = 'X'
        return count
    
    for i in range(vertical):
        for j in range(horizontal):
            if maps[i][j] != 'X':
                result.append(bfs(i, j))
    
    return sorted(result) if result else [-1]