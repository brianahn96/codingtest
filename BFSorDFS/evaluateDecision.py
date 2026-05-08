# Overall Time Complexity: O(Q * (V + E)) where Q is number of queries, V is number of variables, and E is number of equations
# Overall Space Complexity: O(V + E) for storing the graph in a dictionary
# https://leetcode.com/problems/evaluate-division/description/

# Import defaultdict and deque from collections
from collections import defaultdict, deque

# Define the calcEquationDFS function using depth-first search
def calcEquationDFS(equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
    # Initialize a nested dictionary to store the graph with multipliers
    mult = defaultdict(dict)

    # Populate the multipliers dictionary from the equations and values
    for index, (up, down) in enumerate(equations):
            # Store the direct relationship
            mult[up][down] = values[index]
            # Store the reciprocal relationship
            mult[down][up] = 1 / values[index]
    # Print the multipliers for debugging
    print(mult)
    # Define a helper function for DFS
    def dfs(start, end, visited):
        # Base case: if start or end is not in the graph, return -1.0
        if start not in mult or end not in mult:
            # Return -1.0 for invalid query
            return -1.0
        # Base case: if start equals end, the ratio is 1.0
        if start == end:
            # Return 1.0 for same node
            return 1.0
        # Mark the current node as visited
        visited.add(start)

        # Explore neighbors of the current node
        for neighbor, val in mult[start].items():
            # If the neighbor has not been visited yet
            if neighbor not in visited:
                # Recursively call dfs to find path to end
                result = dfs(neighbor, end, visited)
                # If a valid path is found
                if result != -1.0:
                    # Return the cumulative product
                    return result * val
        # If no path is found, return -1.0
        return -1.0

    # Execute DFS for each query and return the results as a list
    return [dfs(a, b, set()) for a, b in queries]

# Define the calcEquationBFS function using breadth-first search
def calcEquationBFS(equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
    # Initialize a nested dictionary to store the graph
    mult = defaultdict(dict)
    
    # Populate the multipliers dictionary from the equations and values
    for index, (up, down) in enumerate(equations):
            # Store the direct relationship
            mult[up][down] = values[index]
            # Store the reciprocal relationship
            mult[down][up] = 1 / values[index]

    # Define a helper function for BFS
    def bfs(start,end):
        # Base case: check if both nodes exist in the graph
        if start not in mult or end not in mult:
            # Return -1.0 if not found
            return -1.0
        
        # Base case: if nodes are the same, ratio is 1.0
        if start == end:
            # Return 1.0
            return 1.0
        
        # Initialize a queue for BFS with (current_node, current_product)
        queue = deque([(start,1.0)])
        # Use a set to keep track of visited nodes
        visited = {start}
        
        # Process nodes in the queue
        while queue:
            # Pop the first element from the queue
            node, curr = queue.popleft()
            
            # Explore neighbors of the current node
            for neighbor, value in mult[node].items():
                # Skip if the neighbor has already been visited
                if neighbor in visited:
                    # Continue to next neighbor
                    continue
                
                # Calculate the result for the neighbor
                result = curr * value
                
                # Check if the target node is reached
                if neighbor == end:
                    # Return the final result
                    return result
                
                # Path compression: update the graph with the direct relationship
                mult[start][neighbor] = result
                # Update with the reciprocal relationship
                mult[neighbor][start] = 1 / result
                
                # Add neighbor to visited set
                visited.add(neighbor)
                # Add neighbor and current product to queue
                queue.append((neighbor,result))
                
        # Return -1.0 if no path is found
        return -1.0
    
    # Execute BFS for each query and return the results as a list
    return [bfs(start,end) for start,end in queries]


# Sample equations for testing
equations = [["a","b"],["b","c"]]
# Sample values for the equations
values = [2.0,3.0]
# Sample queries for testing
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

# Redefine sample data
equations = [["a","b"],["b","c"],["bc","cd"]]
# Redefine sample values
values = [1.5,2.5,5.0]
# Redefine sample queries
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]

# Print the output of calcEquationDFS for testing
print(calcEquationDFS(equations, values, queries))
