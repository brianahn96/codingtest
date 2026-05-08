# Overall Time Complexity: O(N * (N + M)) where N is number of people and M is number of relationships
# Overall Space Complexity: O(N + M) for storing the network adjacency list
# https://www.acmicpc.net/problem/1389

# Import deque from collections for efficient BFS
from collections import deque

# Read the number of people N and the number of relationships M from input
N, M = map(int, input().split())

# Initialize the network adjacency list for N people
network = [[] for _ in range(N + 1)]

# Initialize a list to store the Kevin Bacon results for each person
results = []

# Populate the network adjacency list from M relationships
for i in range(M):
    # Read two people who have a relationship
    j, k = map(int, input().split())
    # Add relationship from j to k
    network[j].append(k)
    # Add relationship from k to j
    network[k].append(j)

# Define the BFS function to calculate the Kevin Bacon number for person i
def bfs(i):
    # Initialize a visited list to store distances, -1 means not visited
    visited = [-1] * (N + 1)

    # Initialize a double-ended queue for BFS
    queue = deque()
    # Add the starting person to the queue
    queue.append(i)
    # Set the distance to self as 0
    visited[i] = 0

    # Process nodes in the queue
    while queue:
        # Pop the leftmost node from the queue
        node = queue.popleft()

        # Iterate through all neighbors of the current node
        for next_node in network[node]:
            # If the neighbor hasn't been visited yet
            if visited[next_node] == -1:
                # Set distance to neighbor as distance to current node + 1
                visited[next_node] = visited[node] + 1
                # Add the neighbor to the queue
                queue.append(next_node)

    # Calculate total Kevin Bacon number (sum of distances) and adjust for 1-based indexing
    total = sum(visited) + 1
    # Return a tuple of the person's index and their total distance sum
    return (i, total)

# Iterate through every person from 1 to N
for i in range(1, N + 1):
    # Append the result of BFS for each person to the results list
    results.append(bfs(i))

# Find the person with the minimum total distance and print their index
print(min(results, key = lambda x: x[1])[0])
