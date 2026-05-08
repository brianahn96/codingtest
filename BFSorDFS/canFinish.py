# Overall Time Complexity: O(V + E) where V is numCourses and E is number of prerequisites
# Overall Space Complexity: O(V + E) for the adjacency list and recursion stack
# https://leetcode.com/problems/course-schedule/

# Import defaultdict from collections module
from collections import defaultdict

# Define the canFinish function
def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:

    # Initialize a defaultdict to store the graph as an adjacency list
    graph = defaultdict(list)

    # Populate the graph with prerequisite relationships
    for x, y in prerequisites:
        # Map course x to its prerequisite y
        graph[x].append(y)

    # Initialize a set to track nodes in the current DFS path (to detect cycles)
    traced = set()
    # Initialize a set to track nodes that have been fully processed
    visited = set()

    # Define the DFS helper function
    def dfs(i):
        # If the current node is in the traced set, a cycle is detected
        if i in traced:
            # Return False indicating a cycle exists
            return False

        # If the node has already been visited and processed, return True
        if i in visited:
            # Return True as no cycle was found from this node
            return True

        # Add the current node to the traced set
        traced.add(i)

        # Explore all prerequisites (neighbors) of the current course
        for y in graph[i]:
            # Recursively call DFS; if it returns False, a cycle was found
            if not dfs(y):
                # Propagation of False to indicate a cycle
                return False

        # After exploring all neighbors, remove the node from the traced set
        traced.remove(i)
        # Mark the node as fully processed in the visited set
        visited.add(i)

        # Return True as no cycle was found starting from this node
        return True

    # Iterate through all courses present in the graph
    for x in list(graph):
        # Call DFS for each course; if it returns False, the schedule is impossible
        if not dfs(x):
            # Return False if any cycle is detected
            return False

    # If no cycles are detected in any paths, return True
    return True
