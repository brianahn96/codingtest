# Overall Time Complexity: O(N) where N is the number of cities
# Overall Space Complexity: O(N) for the adjacency list and tracking sets
# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

# Import defaultdict for adjacency list storage
from collections import defaultdict

# Define the minReorder function to calculate required edge reversals
def minReorder(n: int, connections: list[list[int]]) -> int:
    # Initialize an adjacency list to treat the graph as undirected
    adjacent = defaultdict(list)
    # Initialize a set to store original directed connections
    seen = set()
    # Iterate through each directed connection
    for x, y in connections:
        # Add connection for undirected graph traversal (forward)
        adjacent[x].append(y)
        # Add connection for undirected graph traversal (backward)
        adjacent[y].append(x)
        # Record the original directed connection in the seen set
        seen.add((x, y))

    # Initialize a stack for DFS, starting from city 0
    stack = [0]
    # Initialize a set to keep track of visited cities
    visited = set([0])
    # Initialize the count of edge reversals needed
    ans = 0

    # Process cities in the stack using DFS
    while stack:
        # Pop the last city from the stack
        node = stack.pop()

        # Explore all adjacent cities (neighbors)
        for end in adjacent[node]:
            # If the neighbor has not been visited yet
            if end not in visited:
                # Mark the neighbor as visited
                visited.add(end)
                # If the edge exists in the original direction (node -> end), it needs reversal
                if (node, end) in seen:
                    # Increment the reversal counter
                    ans += 1
                # Add the neighbor to the stack for further DFS
                stack.append(end)

    # Return the total number of reversals calculated
    return ans

# Define sample number of cities
n = 6
# Define sample directed connections
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
# Print the results of minReorder for the sample data
print(minReorder(n, connections))
