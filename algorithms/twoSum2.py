# Overall Time Complexity: O(N) where N is the length of the input numbers list
# Overall Space Complexity: O(1) as we use a constant amount of extra space

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order
# find two numbers such that they add up to a specific target number. 
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

 

# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
# Example 2:

# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
# Example 3:

# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

# Import List from typing to handle the return type and parameter type hints
from typing import List

# Define the twoSum function that takes a sorted list of integers and a target sum
def twoSum(numbers: List[int], target: int) -> List[int]:
    # Initialize the left pointer to the start of the list
    i = 0
    # Initialize the right pointer to the end of the list
    j = len(numbers) - 1
    
    # Continue searching as long as the left pointer is less than the right pointer
    while i < j:
        # Calculate the sum of elements at the current left and right pointers
        s = numbers[i] + numbers[j]
        
        # Check if the calculated sum matches the target value
        if s == target:
            # Return the 1-indexed positions of the two numbers
            return [i + 1, j + 1]
        
        # If the sum is less than the target, move the left pointer forward to increase the sum
        elif s < target:
            # Increment the left pointer by one
            i += 1
        # If the sum is greater than the target, move the right pointer backward to decrease the sum
        else:
            # Decrement the right pointer by one
            j -= 1
