# Overall Time Complexity: O(N) where N is the number of elements in the array
# Overall Space Complexity: O(N) due to the creation of intermediate lists or result arrays

# Define the first version of the rotate function which uses an auxiliary array
def rotate1(nums: list[int], k: int) -> None:
    # Documentation string explaining that the modification should be in-place
    """
    Do not return anything, modify nums in-place instead.
    """
    # Normalize k by taking the modulo with the length of the array
    k %= len(nums)
    # Initialize a result list of the same size as nums with zeros
    res = [0] * len(nums)
    
    # Iterate through each index of the input list
    for i in range(len(nums)):
        # Calculate the new position after rotation and store the value in res
        res[(i + k) % len(nums)] = nums[i]
    
    # Iterate through the input list again to update it with the rotated values
    for i in range(len(nums)):
        # Copy each element from the result list back to the original list
        nums[i] = res[i]
    
# Define the second version of the rotate function which uses reversals
def rotate2(nums: list[int], k: int) -> None:
    # Documentation string explaining that the modification should be in-place
    """
    Do not return anything, modify nums in-place instead.
    """
    # Normalize k by taking the modulo with the length of the array
    k %= len(nums)

    # Reverse the entire list in-place
    nums.reverse()
    
    # Reverse the first k elements of the reversed list
    nums[:k] = nums[:k][::-1]
    # Reverse the remaining n-k elements of the reversed list
    nums[k:] = nums[k:][::-1]
    

# Define the third version of the rotate function which uses slicing and concatenation
def rotate3(nums: list[int], k: int) -> None:
    # Documentation string explaining that the modification should be in-place
    """
    Do not return anything, modify nums in-place instead.
    """
    # Store the length of the list in variable n
    n = len(nums)
    # Normalize k by taking the modulo with n
    k %= n
    # Replace the contents of nums with a slice of the last k elements followed by the first n-k elements
    nums[:] = nums[-k:] + nums[:-k]

# Initialize a sample list of integers
nums = [1,2,3,4,5,6,7]
# Set the number of steps to rotate
k = 3

# Call the second rotation method on the sample list
rotate2(nums, k)
# Print the modified list to verify the rotation
print(nums)
