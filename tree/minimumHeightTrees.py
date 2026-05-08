# Overall Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges
# Overall Space Complexity: O(V + E)

# Source URL for the problem description
# https://leetcode.com/problems/minimum-height-trees/description/

# Import defaultdict from the collections module to represent the graph
from collections import defaultdict

# Function to find the roots of the minimum height trees
def findMinHeightTrees(n: int, edges: list[list[int]]) -> list[int]:
    # Initialize an adjacency list to represent the graph
    graph = defaultdict(list)
    # Iterate through the provided edges
    for u, v in edges:
        # Add edge from u to v
        graph[u].append(v)
        # Add edge from v to u (undirected graph)
        graph[v].append(u)
        
    # Print the constructed graph for debugging purposes
    print(graph)
    
    # Initialize a list to keep track of current leaf nodes
    leaves = []
    # Iterate through all nodes from 0 to n-1
    for i in range(n):
        # Check if the node has exactly one connection (it's a leaf)
        if len(graph[i]) == 1:
            # Add the node to the leaves list
            leaves.append(i)
            
    # Print the initial set of leaves for debugging
    print(leaves)
    
    # Continue removing leaves until only 1 or 2 nodes remain (the roots of MHTs)
    while n > 2:
        # Decrease the total node count by the number of leaves removed
        n -= len(leaves)
        # Initialize a list to store the new set of leaves
        new_leaves = []
        # Iterate through each leaf node in the current set
        for leaf in leaves:
            # Remove the only connection (neighbor) of the leaf node
            neighbor = graph[leaf].pop()
            # Remove the leaf node from its neighbor's adjacency list
            graph[neighbor].remove(leaf)
            
            # Check if the neighbor has now become a leaf node
            if len(graph[neighbor]) == 1:
                # Add the neighbor to the new set of leaves
                new_leaves.append(neighbor)
                
        # Update the leaves list with the newly discovered leaves
        leaves = new_leaves
    
    # Return the remaining nodes (roots of MHTs)
    return leaves
    
# Test case 1 node count
n = 6
# Test case 1 edge list
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]

# Test case 2 node count
n = 4
# Test case 2 edge list
edges = [[1,0],[1,2],[1,3]]

# Print the result of the findMinHeightTrees function
print(findMinHeightTrees(n, edges))
