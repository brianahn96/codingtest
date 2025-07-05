# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

from collections import deque
from typing import List

def numIslands(grid: List[List[str]]) -> int:
    row, col = len(grid), len(grid[0])
    count = 0
    
    def bfs(i, j):
        queue = deque()
        queue.append((i, j))
        dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
        
        
        while queue:
            x, y = queue.popleft()
            
            for k in range(4):
                new_x, new_y = x + dx[k], y + dy[k]
                
                if 0 <= new_x < row and 0 <= new_y < col and grid[new_x][new_y] == "1":
                    queue.append((new_x, new_y))
                    grid[new_x][new_y] = "0"
            grid[x][y] = "0"
    
    for i in range(row):
        for j in range(col):
            if grid[i][j] == "1":
                bfs(i, j)
                count += 1
    
    return count