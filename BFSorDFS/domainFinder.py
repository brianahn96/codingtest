# Overall Time Complexity: O(M * N + K * (y2-y1)*(x2-x1)) where M*N is grid size and K is number of rectangles
# Overall Space Complexity: O(M * N) for the graph grid and BFS queue
# https://www.acmicpc.net/problem/2583

# Import deque from collections for efficient queue operations
from collections import deque

# Read grid dimensions M, N and number of rectangles K
M, N, K = map(int, input().split())
# Initialize the M x N grid with zeros
graph = [[0] * N for _ in range(M)]
# Initialize a list to store the areas of empty regions
result = []

# Process each of the K rectangles
for _ in range(K):
    # Read the coordinates of the current rectangle
    x1, y1, x2, y2 = map(int, input().split())
    # Iterate through the height of the rectangle
    for i in range(y1, y2):
        # Iterate through the width of the rectangle
        for j in range(x1, x2):
            # Mark the cell as part of a rectangle (non-zero)
            graph[i][j] += 1
            
# Define the BFS function to find the area of an empty region
def bfs(i, j):
    # Initialize the area count to 1 for the starting cell
    count = 1
    # Initialize a queue for BFS and add the starting coordinates
    queue = deque()
    # Append the starting (y, x) coordinates to the queue
    queue.append((i, j))
    # Define relative movements in the x-direction (left, right)
    diff_x = [-1, 0, 1, 0]
    # Define relative movements in the y-direction (up, down)
    diff_y = [0, 1, 0, -1]
    # Continue while there are coordinates to process in the queue
    while queue:
        # Pop the leftmost (y, x) coordinates from the queue
        y, x = queue.popleft()
        # Check all four possible movement directions
        for k in range(4):
            # Calculate the new coordinates
            new_y, new_x = y + diff_y[k], x + diff_x[k]
            # Check if the new coordinates are within bounds and the cell is empty (0)
            if (0 <= new_y < M) and (0 <= new_x < N) and graph[new_y][new_x] == 0:
                # Mark the empty cell as visited
                graph[new_y][new_x] += 1
                # Append the new coordinates to the queue
                queue.append((new_y, new_x))
                # Increment the area count
                count += 1
    # Return the total area of the empty region
    return count

# Iterate through each cell in the grid
for i in range(M):
    # Iterate through each column in the grid
    for j in range(N):
        # If the cell is empty, start a BFS to find the area of the region
        if graph[i][j] == 0:
            # Mark the current cell as visited
            graph[i][j] = 1
            # Add the area of the region to the results list
            result.append(bfs(i, j))

# Print the number of disconnected empty regions found
print(len(result))
# Print the sorted areas of all empty regions
print(*sorted(result))
