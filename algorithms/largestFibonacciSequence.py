# Overall Time Complexity: O(N + log(max_val)) where N is the number of elements in arr and max_val is the maximum element
# Overall Space Complexity: O(N + log(max_val)) to store the Fibonacci set and the resulting subset list

# Link to the problem description on GeeksforGeeks
# https://www.geeksforgeeks.org/problems/largest-fibonacci-subsequence2206/1

# Define a function to find the subset of an array that contains only Fibonacci numbers
def findFibSubset(arr):
    # Retrieve the maximum value from the input array to determine the range of Fibonacci numbers needed
    max_val = max(arr)
    
    # Initialize a list with the first two numbers of the Fibonacci sequence
    fib = [0, 1]
    # Generate Fibonacci numbers until the last number in the list is at least the maximum value in the array
    while fib[-1] < max_val:
        # Append the sum of the last two Fibonacci numbers to the list
        fib.append(fib[-1] + fib[-2])

    # Convert the list of Fibonacci numbers into a set for O(1) average time complexity lookups
    fib_set = set(fib)

    # Use a list comprehension to filter the input array, keeping only elements present in the Fibonacci set
    res = [x for x in arr if x in fib_set]

    # Return the list of elements that are part of the Fibonacci sequence
    return res
