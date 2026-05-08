# Overall Time Complexity: O(V * (V + E)) where V is vertices and E is edges, due to list lookup in 'discovered'
# Overall Space Complexity: O(V), to store the 'discovered' list and the recursion stack, stack, or queue

# Define the graph structure using an adjacency list where each key is a node and its value is a list of its neighbors
graph = {
    # Node 1 is connected to nodes 2, 3, and 4
    1:[2,3,4],
    # Node 2 is connected to node 5
    2:[5],
    # Node 3 is connected to node 5
    3:[5],
    # Node 4 has no outgoing connections
    4:[],
    # Node 5 is connected to nodes 6 and 7
    5:[6,7],
    # Node 6 has no outgoing connections
    6:[],
    # Node 7 is connected to node 3
    7:[3]
}

# Define a function to perform Depth-First Search recursively
def recursive_dfs(graph, v, discovered = []):
    # Add the current node 'v' to the list of discovered nodes
    discovered.append(v)
    # Iterate through each neighbor 'w' of the current node 'v'
    for w in graph[v]:
        # Check if the neighbor 'w' has already been discovered
        if not w in discovered:
            # Recursively call DFS starting from the undiscovered neighbor 'w'
            discovered = recursive_dfs(graph, w, discovered)
    # Return the final list of discovered nodes after the recursive calls finish
    return discovered

# Define a function to perform Depth-First Search iteratively using a stack
def iterative_dfs(graph, start_v):
    # Initialize an empty list to keep track of nodes that have been visited
    discovered = []
    # Initialize a stack with the starting node to manage the order of exploration
    stack = [start_v]
    # Continue the loop as long as there are nodes remaining in the stack
    while stack:
        # Remove and return the last node added to the stack (LIFO behavior)
        v = stack.pop()
        # Check if the node 'v' has already been recorded as discovered
        if v not in discovered:
            # Append the newly discovered node 'v' to the discovered list
            discovered.append(v)
            # Iterate through each neighbor 'w' of the current node 'v'
            for w in graph[v]:
                # Add the neighbor 'w' to the stack to be visited in subsequent iterations
                stack.append(w)
    # Return the list of all nodes discovered during the iterative process
    return discovered

# Define a function to perform Breadth-First Search iteratively using a queue
def iterative_bfs(graph, start_v):
    # Initialize the discovered list with the starting node 'start_v'
    discovered = [start_v]
    # Initialize a queue with the starting node to manage the exploration order
    queue = [start_v]
    
    # Process nodes in the queue until no more nodes are left (queue is empty)
    while queue:
        # Remove and return the first node added to the queue (FIFO behavior)
        v = queue.pop(0)
        # Iterate through every neighbor 'w' of the current node 'v'
        for w in graph[v]:
            # Check if the neighbor 'w' has already been added to the discovered list
            if w not in discovered:
                # Mark the neighbor 'w' as discovered by adding it to the list
                discovered.append(w)
                # Append the neighbor 'w' to the queue for future level-by-level exploration
                queue.append(w)
    # Return the complete list of nodes discovered in breadth-first order
    return discovered
