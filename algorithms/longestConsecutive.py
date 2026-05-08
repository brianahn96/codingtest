# Overall Time Complexity: O(N) where N is the number of elements in the input list
# Overall Space Complexity: O(N) to store the set of numbers for efficient lookup

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

# Define a function to find the length of the longest consecutive sequence in a list of integers
def longestConsecutive(nums: list[int]) -> int:
    # Initialize a variable to store the maximum length of a consecutive sequence found
    longest = 0
    # Create a set from the input list to allow for O(1) average time complexity element lookups
    num_set = set(nums)

    # Iterate through each unique number present in the set
    for n in num_set:
        # Check if the current number is the start of a sequence by ensuring the predecessor is not in the set
        if n - 1 not in num_set:
            # Initialize the length of the current sequence to 1
            length = 1
            # Continue incrementing the length as long as the next consecutive number exists in the set
            while n+length in num_set:
                # Increment the current sequence length
                length += 1
            # Update the global longest sequence length if the current sequence is longer
            longest = max(longest, length)
    # Return the length of the longest consecutive sequence identified
    return longest
