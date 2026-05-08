# Overall Time Complexity: O(M * N) where M and N are dimensions of the grid
# Overall Space Complexity: O(M * N) for the BFS queue in the worst case
# https://leetcode.com/problems/rotting-oranges/description/

# Import List for type hinting
from typing import List

# Define the orangesRotting function
def orangesRotting(grid: List[List[int]]) -> int:
    # Initialize a list to act as a queue for BFS
    queue = []
    # Initialize answer to -1 to account for the first increment
    ans = -1
    # Get the number of rows M and columns N of the grid
    M, N = len(grid), len(grid[0])
    # Iterate through each row in the grid
    for i in range(M):
        # Iterate through each column in the grid
        for j in range(N):
            # If the current cell contains a rotten orange (value 2)
            if grid[i][j] == 2:
                # Add the coordinates of the rotten orange to the queue
                queue.append((i, j))

    # Define the four possible movement directions: up, down, left, right
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    # Continue BFS as long as there are rotten oranges in the queue
    while queue:
        # Create a copy of the current queue to process one minute's worth of rotting
        rotten = queue.copy()
        # Clear the original queue to store the next set of rotten oranges
        queue.clear()

        # Iterate through each currently rotten orange
        for x, y in rotten:
            # Check all four adjacent cells
            for i in range(4):
                # Calculate the coordinates of the adjacent cell
                new_x, new_y = x + dx[i], y + dy[i]
                # Check if coordinates are within bounds and the orange is fresh (value 1)
                if 0 <= new_x < M and 0 <= new_y < N and grid[new_x][new_y] == 1:
                    # Mark the fresh orange as rotten
                    grid[new_x][new_y] = 2
                    # Add the newly rotten orange to the queue for the next minute
                    queue.append((new_x, new_y))
        # Increment the time counter by one minute
        ans += 1
        
    # After the process, check if any fresh oranges remain
    for i in grid:
        # Iterate through each cell in the row
        for j in i:
            # If a fresh orange is found
            if j == 1:
                # Return -1 because not all oranges can rot
                return - 1
    # If no rotten oranges were ever processed (ans == -1), return 0; otherwise return ans
    return ans if ans != -1 else 0
