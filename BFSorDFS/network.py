# Overall Time Complexity: O(n^2) where n is number of computers (due to adjacency matrix)
# Overall Space Complexity: O(n^2) for the input adjacency matrix and O(n) for visited tracking
# https://school.programmers.co.kr/learn/courses/30/lessons/154540

# Define the solution function to find the number of connected networks
def solution(n, computers):
    # Initialize the count of networks
    answer = 0
    # Initialize a list to keep track of visited computers
    visited = [False] * n
    
    # Define the DFS helper function (using a stack)
    def dfs(i):
        # Initialize an empty stack for DFS
        stack = []
        # Add the starting computer index to the stack
        stack.append(i)
        
        # Continue DFS until the stack is empty
        while stack:
            # Pop the last computer index from the stack
            last = stack.pop()
            # Mark the current computer as visited
            visited[last] = True
            # Iterate through all computers to check for connections
            for idx, node in enumerate(computers[last]):
                # If the computer is not visited and is connected (node is 1)
                if not visited[idx] and node:
                    # Add the connected computer to the stack for further exploration
                    stack.append(idx)
        
    # Iterate through each computer
    for node in range(n):
        # If the computer has not been visited yet
        if not visited[node]:
            # Perform DFS to mark all computers in the same network
            dfs(node)
            # Increment the count of networks found
            answer += 1
    # Return the total number of connected networks
    return answer
