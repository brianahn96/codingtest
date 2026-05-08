# Overall Time Complexity: O(M + log N) where M is the number of rows (due to the map operation) and N is the number of columns
# Overall Space Complexity: O(M) to store the first elements of each row in the 'firstrows' list

# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.


# Example 1:

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

# Define a function to search for a target value in a specialized sorted 2D matrix
def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    # Extract the first element of every row into a separate list for row-level binary search
    firstrows = list(map(lambda x: x[0], matrix))

    # Initialize left and right pointers for binary search on the first elements of the rows
    left, right = 0, len(firstrows) - 1

    # Perform binary search to identify which row might contain the target value
    while left <= right:
        
        # Check if either the left or right boundary value matches the target
        if firstrows[left] == target or firstrows[right] == target:
            # Return True if a match is found at the boundaries
            return True
        
        # Calculate the middle index for the row-level binary search
        mid = (left + right) // 2

        # If the middle row's first element is less than the target, narrow search to the right half
        if firstrows[mid] < target:
            # Move the left pointer to mid + 1
            left = mid + 1
        # If the middle row's first element is greater than the target, narrow search to the left half
        elif firstrows[mid] > target:
            # Move the right pointer to mid - 1
            right = mid - 1
        # If the middle row's first element exactly matches the target, return True
        else:
            # Target found at the start of the middle row
            return True

    # Select the row that could potentially contain the target based on the search results
    row = matrix[right] if target > firstrows[right] else matrix[left]
    
    # Reset left and right pointers for binary search within the identified row
    left, right = 0, len(row) - 1
    
    # Perform binary search within the selected row to find the target value
    while left <= right:
        # Calculate the middle index for the element-level binary search
        mid = (left + right) // 2
        
        # If the middle element is less than the target, narrow search to the right half
        if row[mid] < target:
            # Move the left pointer to mid + 1
            left = mid + 1
        # If the middle element is greater than the target, narrow search to the left half
        elif row[mid] > target:
            # Move the right pointer to mid - 1
            right = mid - 1
        # If the middle element exactly matches the target, return True
        else:
            # Target successfully found within the row
            return True
    # Return False if the target was not found after both search phases
    return False
