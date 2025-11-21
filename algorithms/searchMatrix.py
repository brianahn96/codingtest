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

from typing import List

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    firstrows = list(map(lambda x: x[0], matrix))

    left, right = 0, len(firstrows) - 1

    while left <= right:
        
        if firstrows[left] == target or firstrows[right] == target:
            return True
        
        mid = (left + right) // 2

        if firstrows[mid] < target:
            left = mid + 1
        elif firstrows[mid] > target:
            right = mid - 1
        else:
            return True

    row = matrix[right] if target > firstrows[right] else matrix[left]
    
    left, right = 0, len(row) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if row[mid] < target:
            left = mid + 1
        elif row[mid] > target:
            right = mid - 1
        else:
            return True
    return False
    