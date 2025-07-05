# https://leetcode.com/problems/rotting-oranges/description/

from typing import List

def orangesRotting(grid: List[List[int]]) -> int:
    queue = []
    ans = -1
    M, N = len(grid), len(grid[0])
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 2:
                queue.append((i, j))

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    while queue:
        rotten = queue.copy()
        queue.clear()

        for x, y in rotten:
            for i in range(4):
                new_x, new_y = x + dx[i], y + dy[i]
                if 0 <= new_x < M and 0 <= new_y < N and grid[new_x][new_y] == 1:
                    grid[new_x][new_y] = 2
                    queue.append((new_x, new_y))
        ans += 1
    for i in grid:
        for j in i:
            if j == 1:
                return - 1
    return ans if ans != -1 else 0