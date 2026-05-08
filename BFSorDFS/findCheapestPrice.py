# Overall Time Complexity: O(E * K * log(E * K)) where E is number of flights and K is at most k stops
# Overall Space Complexity: O(N + E * K) for graph storage and priority queue
# There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

# You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.


# Example 1:

# Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
# Output: 700
# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
# Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

# Example 2:

# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
# Output: 200
# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

# Example 3:

# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
# Output: 500
# Explanation:
# The graph is shown above.
# The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.

# Import List for type hinting
from typing import List
# Import heapq for priority queue operations
import heapq

# Define the findCheapestPrice function
def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    # Initialize an adjacency list for the graph
    graph = [[] for _ in range(n)]

    # Populate the graph with flight information
    for u, v, w in flights:
        # Append destination and price to the source city's list
        graph[u].append((v, w))

    # Initialize priority queue with (price, current_node, stops_remaining)
    queue = [(0, src, k)]

    # Continue processing while the priority queue is not empty
    while queue:
        # Pop the flight with the minimum current price
        price, node, distance = heapq.heappop(queue)
        # If the destination city is reached, return the price
        if node == dst:
            # Return the cheapest price found
            return price
        # If there are still stops allowed (distance >= 0)
        if distance >= 0:
            # Explore neighbors of the current node
            for v, w in graph[node]:
                # Calculate the new price to the neighbor
                alt = price + w
                # Push the neighbor into the priority queue with one less stop allowed
                heapq.heappush(queue, (alt, v, distance - 1))

    # If the destination is never reached within k stops, return -1
    return -1
