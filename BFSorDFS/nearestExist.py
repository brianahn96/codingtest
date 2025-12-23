# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/description/

from collections import deque

def nearestExit(maze: list[list[str]], entrance: list[int]) -> int:
    row_length, column_length = len(maze), len(maze[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()
    queue = deque()
    queue.append((entrance[0], entrance[1], 0))

    while queue:
        row, column, count = queue.popleft()

        if (row, column) in visited:
            continue

        if maze[row][column] == "+":
            continue
            
        if not (row == entrance[0] and column == entrance[1]) and (row == 0 or row == row_length - 1 or column == 0 or column == column_length - 1):
            return count

        visited.add((row, column))

        for x, y in directions:
            move_row, move_column = row + x, column + y
            if move_row >= 0 and move_row < row_length and move_column >=0 and move_column < column_length:
                queue.append((move_row, move_column, count + 1))

    return -1
