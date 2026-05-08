# Overall Time Complexity: O(k * C(n, k)) where C(n, k) is the number of combinations
# Overall Space Complexity: O(k) for recursion stack and temporary element storage
# https://leetcode.com/problems/combinations/description/

# Define the combine function to find all combinations of k numbers from 1 to n
def combine(n: int, k: int) -> list[list[int]]:
    # Initialize the list to store all valid combinations
    results = []
    
    # Define a helper function for depth-first search
    def dfs(elements, start: int, k: int):
        # Base case: if k is zero, a complete combination has been formed
        if k == 0:
            # Append a copy of the current combination to results
            results.append(elements[:])
            # Return to continue searching for other combinations
            return
            
        # Iterate from the start index to n to pick numbers for the combination
        for i in range(start, n + 1):
            # Add the current number to the combination
            elements.append(i)
            # Recursively call dfs to pick the next number, incrementing start and decrementing k
            dfs(elements, i + 1, k - 1)
            # Remove the last number to backtrack and try the next possibility
            elements.pop()
    
    # Start the DFS with an empty list, starting number 1, and target size k
    dfs([], 1, k)
    # Return the final list of combinations
    return results
