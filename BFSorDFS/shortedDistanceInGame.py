# Overall Time Complexity: O(M * N) where M and N are dimensions of the maps
# Overall Space Complexity: O(M * N) for the BFS queue in the worst case
# https://school.programmers.co.kr/learn/courses/30/lessons/1844

# Import deque from collections for efficient BFS
from collections import deque

# Define the solution function to find the shortest path in the grid
def solution(maps):
    # Determine the dimensions M (rows) and N (columns) of the map
    M, N = len(maps), len(maps[0])
    # Initialize a queue for BFS
    queue = deque()
    # Add the starting point (0, 0) to the queue
    queue.append((0,0))
    # Define movement directions: left, right, up, down
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    # Process nodes in the queue while it's not empty
    while queue:
        # Pop the leftmost coordinates (x, y) from the queue
        x, y = queue.popleft()
        # Explore each of the 4 possible directions
        for i in range(4):
            # Calculate the new coordinates based on direction
            new_x, new_y = x + dx[i], y + dy[i]
            # Check if new coordinates are within bounds and the cell is reachable (value is 1)
            if 0 <= new_x < M and 0 <= new_y < N and maps[new_x][new_y] == 1:
                # Add the new coordinates to the queue
                queue.append((new_x, new_y))
                # Update the cell value with the distance from the starting point
                maps[new_x][new_y] = maps[x][y] + 1
        
    # Get the value at the target destination (bottom-right corner)
    answer = maps[M - 1][N - 1]
    
    # Return the distance if reachable (value > 1), otherwise return -1
    return answer if answer != 1 else -1
