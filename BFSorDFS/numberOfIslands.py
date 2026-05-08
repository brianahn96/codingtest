# Overall Time Complexity: O(M * N), where M is the number of rows and N is the number of columns in the grid
# Overall Space Complexity: O(min(M, N)) for the BFS queue, and O(M * N) in the worst case for the DFS recursion stack

# Import the deque class for implementing Breadth-First Search
from collections import deque
# Import the List type for accurate function signatures and type hinting
from typing import List

# Define a function to count islands using a BFS approach
def numIslands(grid: List[List[str]]) -> int:
    # Retrieve the dimensions of the grid: rows and columns
    row, col = len(grid), len(grid[0])
    # Initialize a variable to track the total number of islands
    count = 0
    
    # Define an inner function to perform BFS from a starting land cell
    def bfs(i, j):
        # Create a queue and add the starting cell coordinates
        queue = deque()
        # Append the initial coordinates to the queue
        queue.append((i, j))
        # Define the relative shifts for moving in 4 directions: up, down, right, and left
        dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
        
        # Continue the process while there are cells in the queue to visit
        while queue:
            # Extract the next set of coordinates from the left side of the queue
            x, y = queue.popleft()
            
            # Loop through each of the four possible movement directions
            for k in range(4):
                # Compute the coordinates for the adjacent cell
                new_x, new_y = x + dx[k], y + dy[k]
                
                # Check if the new cell is within grid boundaries and is land ('1')
                if 0 <= new_x < row and 0 <= new_y < col and grid[new_x][new_y] == "1":
                    # Add the valid land cell to the queue for future exploration
                    queue.append((new_x, new_y))
                    # Mark the cell as water ('0') immediately to prevent redundant visits
                    grid[new_x][new_y] = "0"
                    
            # Ensure the current cell is also marked as water
            grid[x][y] = "0"
    
    # Loop through each row in the grid
    for i in range(row):
        # Loop through each column within the current row
        for j in range(col):
            # If a land cell is encountered, it represents a new island
            if grid[i][j] == "1":
                # Execute BFS to sink the entire island
                bfs(i, j)
                # Increment the total island count
                count += 1
    
    # Return the total number of islands identified
    return count

# Define a function to count islands using a DFS approach
def numIslandsDFS(grid: List[List[str]]) -> int:
    # Define a recursive helper function for Depth-First Search
    def dfs(i, j):
        # Base case: if out of bounds or the cell is not land, return
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "1":
            # Exit the current recursion level
            return
        
        # Sink the current land cell by changing it to water ('0')
        grid[i][j] = "0"
        
        # Recursively visit the cell directly below
        dfs(i + 1, j)
        # Recursively visit the cell directly above
        dfs(i - 1, j)
        # Recursively visit the cell to the right
        dfs(i, j + 1)
        # Recursively visit the cell to the left
        dfs(i, j - 1)
        
    # Initialize a variable to track the total number of islands
    count = 0
    
    # Iterate through every row index of the grid
    for i in range(len(grid)):
        # Iterate through every column index of the current row
        for j in range(len(grid[0])):
            # If a land cell is found, it signifies a new island
            if grid[i][j] == "1":
                # Execute DFS to sink the entire island recursively
                dfs(i, j)
                # Increment the island count
                count += 1
    
    # Return the final number of islands counted
    return count
