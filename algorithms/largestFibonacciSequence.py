# https://www.geeksforgeeks.org/problems/largest-fibonacci-subsequence2206/1

def findFibSubset(arr):
    # code here
    max_val = max(arr)
    
    fib = [0, 1]
    while fib[-1] < max_val:
        fib.append(fib[-1] + fib[-2])

    fib_set = set(fib)

    res = [x for x in arr if x in fib_set]

    return res