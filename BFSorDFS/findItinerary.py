# Overall Time Complexity: O(E log E), where E is the number of tickets (due to sorting edges)
# Overall Space Complexity: O(V + E), where V is the number of airports and E is the number of tickets

# Import the defaultdict class from the collections module to handle missing keys gracefully
from collections import defaultdict

# Define a function to reconstruct the itinerary given a list of tickets
def findItinerary(tickets: list[list[str]]) -> list[str]:
    # Initialize a graph using a dictionary where each key maps to a list of destinations
    graph = defaultdict(list)
    # Sort the tickets in reverse lexicographical order and iterate through them
    for a, b in sorted(tickets, reverse=True):
        # Add the destination airport to the list of reachable airports for the source airport
        graph[a].append(b)
    # Initialize an empty list to store the sequence of airports in the final route
    route = []

    # Define a helper function to perform Hierholzer's algorithm using Depth First Search
    def dfs(a):
        # Continue exploring while there are still available destinations from the current airport
        while graph[a]:
            # Pop the lexicographically smallest airport (last in the reverse-sorted list) and recurse
            dfs(graph[a].pop())
        # Append the current airport to the route after all outgoing edges have been explored
        route.append(a)

    # Begin the traversal starting from the "JFK" airport
    dfs("JFK")
    # Return the accumulated route in reverse order to get the correct sequence from start to finish
    return route[::-1]
