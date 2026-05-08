# Overall Time Complexity: O(M * N), where M is the number of rows and N is the number of columns
# Overall Space Complexity: O(M * N), to store the maze graph and the BFS queue

# Import the deque class from the collections module to facilitate efficient BFS queue operations
from collections import deque

# Read the maze dimensions (M rows and N columns) from the user input and split into two integers
M, N = map(int, input().split())
# Initialize an empty list that will serve as the 2D grid representation of the maze
graph = []

# Loop through the range of M rows to populate the maze graph
for i in range(M):
    # Read each row of the maze, convert it into a list of integers, and add it to the graph
    graph.append(list(map(int,input())))

# Define a function to perform Breadth-First Search to find the shortest path in the maze
def bfs(i, j):
    # Create a deque object for the BFS queue and initialize it with the starting coordinates
    queue = deque()
    # Add the initial coordinates (i, j) to the queue
    queue.append((i, j))
    # Define the movement offsets for x-coordinates for moving in four directions
    diff_x = [-1, 0, 1, 0]
    # Define the movement offsets for y-coordinates for moving in four directions
    diff_y = [0, 1, 0, -1]
    
    # Process coordinates in the queue until it is empty
    while queue:
        # Extract the next set of coordinates from the front of the queue
        x, y = queue.popleft()
        
        # Iterate through the four possible movement directions (up, right, down, left)
        for i in range(4):
            # Calculate the new x and y coordinates based on the current direction
            new_x, new_y = x + diff_x[i], y + diff_y[i]
            
            # Check if the new coordinates are within maze boundaries and mark an unvisited path (1)
            if 0 <= new_x < M and 0 <= new_y < N and graph[new_x][new_y] == 1:
                # Update the neighbor cell with its distance from the start (current cell's value + 1)
                graph[new_x][new_y] = graph[x][y] + 1
                # Add the neighbor's coordinates to the queue to explore its neighbors later
                queue.append((new_x, new_y))
    
    # Return the accumulated distance value found at the bottom-right exit of the maze
    return graph[M - 1][N - 1]

# Start the BFS search from the top-left corner (0, 0) and output the shortest path length
print(bfs(0,0))
