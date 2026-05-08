# Overall Time Complexity: O(N^2), where N is the number of cities (length of isConnected)
# Overall Space Complexity: O(N), for the visited set and DFS stack

# Import the deque class from the collections module
from collections import deque

# Define a function to find the number of provinces (connected components)
def findCircleNum(isConnected: list[list[int]]) -> int:
    # Initialize a variable to keep track of the number of provinces found
    ans = 0
    # Initialize a set to store the indices of cities that have been visited
    visited = set()

    # Define an inner helper function to perform Depth First Search starting from a given index
    def dfs(index):
        # Initialize a stack for iterative DFS with the starting city index
        stack = [index]
        # Add the starting city index to the visited set
        visited.add(index)

        # Loop until there are no more cities to explore in the current province
        while stack:
            # Pop the last city index from the stack to explore its neighbors
            vertex = stack.pop()
            # Iterate through all possible cities in the isConnected matrix
            for neighbor in range(len(isConnected)):
                # Check if the neighbor city is connected to the current vertex and has not been visited
                if neighbor not in visited and isConnected[vertex][neighbor] == 1:
                    # Mark the neighbor city as visited
                    visited.add(neighbor)
                    # Push the neighbor city index onto the stack for further exploration
                    stack.append(neighbor)

    # Iterate through every city index in the input list
    for i in range(len(isConnected)):
        # If the city has not been visited yet, it belongs to a new province
        if i not in visited:
            # Start a DFS to explore and mark all cities connected to the current city
            dfs(i)
            # Increment the province counter by one
            ans += 1
    # Return the total number of provinces identified
    return ans
