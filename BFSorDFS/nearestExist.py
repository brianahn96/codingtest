# Overall Time Complexity: O(M * N) where M and N are dimensions of the maze
# Overall Space Complexity: O(M * N) for the visited set and BFS queue
# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/description/

# Import deque from collections for efficient queue operations
from collections import deque

# Define the nearestExit function to find the shortest path to an exit
def nearestExit(maze: list[list[str]], entrance: list[int]) -> int:
    # Determine the number of rows and columns in the maze
    row_length, column_length = len(maze), len(maze[0])
    # Define the four possible movement directions: right, left, down, up
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # Initialize a set to keep track of visited coordinates
    visited = set()
    # Initialize a queue for BFS
    queue = deque()
    # Add the starting entrance coordinates and step count 0 to the queue
    queue.append((entrance[0], entrance[1], 0))

    # Process nodes in the queue while it's not empty
    while queue:
        # Pop the leftmost element (row, column, current steps) from the queue
        row, column, count = queue.popleft()

        # If the current cell has already been visited, skip it
        if (row, column) in visited:
            # Move to the next element in the queue
            continue

        # If the current cell is a wall ("+"), skip it
        if maze[row][column] == "+":
            # Move to the next element in the queue
            continue
            
        # Check if the current cell is an exit (on the boundary) and not the entrance
        if not (row == entrance[0] and column == entrance[1]) and (row == 0 or row == row_length - 1 or column == 0 or column == column_length - 1):
            # Return the number of steps taken to reach the exit
            return count

        # Mark the current cell as visited
        visited.add((row, column))

        # Explore all four possible directions from the current cell
        for x, y in directions:
            # Calculate the coordinates of the new position
            move_row, move_column = row + x, column + y
            # Check if the new coordinates are within the maze boundaries
            if move_row >= 0 and move_row < row_length and move_column >=0 and move_column < column_length:
                # Add the new coordinates and incremented step count to the queue
                queue.append((move_row, move_column, count + 1))

    # If no exit is reachable, return -1
    return -1
