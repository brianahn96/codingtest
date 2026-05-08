# Overall Time Complexity: O(log N) where N is the number of elements in the input list
# Overall Space Complexity: O(1) as it uses a constant amount of extra space

# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
# For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

 
# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

# Example 2:

# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

# Example 3:

# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

# Define a function to find the minimum element in a rotated sorted array using binary search
def findMin(nums: list[int]) -> int:
    # Initialize left and right pointers to the start and end of the list
    left, right = 0, len(nums) - 1
    
    # Execute binary search loop as long as the search space is valid
    while left <= right:
        # Calculate the middle index of the current search range
        mid = (left + right) // 2
        
        # Check if the element immediately following mid is the minimum (inflection point)
        if nums[mid + 1] < nums[mid]:
            # Return the element at mid + 1 as the minimum
            return nums[mid + 1]
        # Check if the element at mid itself is the minimum compared to its predecessor
        if nums[mid] < nums[mid - 1]:
            # Return the element at mid as the minimum
            return nums[mid]
        
        # If the rightmost element is greater than the middle element, the minimum is in the left half
        if nums[right] > nums[mid]:
            # Narrow the search range to the left of mid
            right = mid - 1
        # Otherwise, the inflection point and minimum are in the right half
        else:
            # Narrow the search range to the right of mid
            left = mid + 1
            

# Define an alternative, cleaner implementation for finding the minimum in a rotated sorted array
def findMin2(nums: list[int]) -> int:
    # Initialize left and right pointers to the start and end of the list
    left, right = 0, len(nums) - 1

    # Continue searching as long as left index is less than right index
    while left < right:
        # Calculate middle index with potential overflow prevention
        mid = left + (right - left) // 2

        # If mid element is greater than rightmost element, the minimum must be to the right
        if nums[mid] > nums[right]:
            # Move the left pointer past mid
            left = mid + 1
        # If mid element is less than or equal to rightmost, the minimum is at mid or to the left
        else:
            # Set right pointer to mid
            right = mid

    # Return the element at the index where the pointers converged
    return nums[left]

# Define a sample rotated sorted list for testing
nums = [3,4,5,1,2]
# Print the result of the first findMin function
print(findMin(nums))
# Print the result of the second findMin2 function
print(findMin2(nums))
