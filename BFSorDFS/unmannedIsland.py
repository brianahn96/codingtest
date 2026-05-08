# Overall Time Complexity: O(R * C * (R * C)), where R is rows and C is columns (due to list lookup in visited)
# Overall Space Complexity: O(R * C), for the maps copy, queue, and visited list

# Import the deque class from the collections module for efficient queue management
from collections import deque

# Define the function to solve the island food problem
def solution(maps):
    # Calculate the number of rows (vertical) and columns (horizontal) in the map
    vertical, horizontal = len(maps), len(maps[0])
    # Convert each row string into a list of characters to allow for in-place modifications
    maps = [list(map(str, maps[i])) for i in range(len(maps))]
    # Initialize lists representing the four cardinal directions for movement
    dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
    # Initialize an empty list to store the total food count for each distinct island found
    result = []
    
    # Define a Breadth-First Search helper function to traverse an entire island
    def bfs(i, j):
        # Create a new deque object to serve as the queue for BFS
        queue = deque()
        # Add the starting coordinates of the island to the queue
        queue.append((i, j))
        # Initialize an empty list to track coordinates visited during this specific BFS traversal
        visited = []
        # Initialize a counter to sum the food values found on this island
        count = 0
        
        # Continue the search while there are still unexplored parts of the island in the queue
        while queue:
            # Remove the first set of coordinates from the queue for inspection
            x, y = queue.popleft()
            # Iterate through the four possible movement directions
            for i in range(4):
                # Calculate the potential new coordinates based on the movement offsets
                new_x, new_y = x + dx[i], y + dy[i]
                # Validate the new coordinates: within bounds, not visited in this BFS, and not sea ('X')
                if 0 <= new_x < vertical and 0 <= new_y < horizontal and (new_x, new_y) not in visited and maps[new_x][new_y] != 'X':
                    # Add the valid new coordinates to the queue for future processing
                    queue.append((new_x, new_y))
                    # Record the new coordinates as visited to prevent redundant processing
                    visited.append((new_x, new_y))

            # Add the numeric food value of the current cell to the island's total count
            count += int(maps[x][y])
            # Mark the current cell as sea ('X') to ensure it is not processed in future BFS searches
            maps[x][y] = 'X'
        # Return the accumulated food count for the current island
        return count
    
    # Iterate through every row index of the map
    for i in range(vertical):
        # Iterate through every column index within the current row
        for j in range(horizontal):
            # If the current cell contains food (is not 'X'), it marks the start of an island
            if maps[i][j] != 'X':
                # Call BFS to find the total food on the island and append the result to the list
                result.append(bfs(i, j))
    
    # Return the sorted list of food counts, or [-1] if no islands were discovered
    return sorted(result) if result else [-1]
