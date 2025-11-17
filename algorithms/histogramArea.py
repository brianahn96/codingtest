# Have the function HistogramArea(arr) read the array of non-negative integers stored in arr which will represent the heights of bars on a graph (where each bar width is 1)
# and determine the largest area underneath the entire bar graph.
# You can see in the above bar graph that the largest area underneath the graph is covered by the x's. 
# The area of that space is equal to 6 because the entire width is 2 and the maximum height is 3, therefore 2 * 3 = 6. 
# Your program should return 6. The array will always contain at least 1 element.

def HistogramArea(arr):

    # Stack to keep track of indices
    stack = []

    # Initialize max area
    max_area = 0

    # Iterate through the array
    for i in range(len(arr)):
        # Pop elements from the stack while the stack is not empty and the current bar is smaller than the bar at the top of the stack
        while stack and arr[i] < arr[stack[-1]]:
            height = arr[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)

        # Push the current index onto the stack
        stack.append(i)

    # Pop the remaining elements from the stack and calculate area
    while stack:
        height = arr[stack.pop()]
        width = len(arr) if not stack else len(arr) - stack[-1] - 1
        max_area = max(max_area, height * width)

    return max_area

# Example usage
arr = [2, 1, 2, 3, 1]
result = HistogramArea(arr)
print(result)
