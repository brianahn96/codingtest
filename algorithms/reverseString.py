# Overall Time Complexity: O(N) where N is the length of the list s
# Overall Space Complexity: O(1) as the modification is performed in-place with constant extra space

# Link to the problem description on LeetCode
#  https://leetcode.com/problems/reverse-string/

# Import List from the typing module for type hinting the function parameter
from typing import List

# Define a function to reverse a list of characters in-place
def reverseString(s: List[str]) -> None:
    # Initialize two pointers, left starting at the beginning and right at the end of the list
    left, right = 0, len(s) - 1
    
    # Continue swapping elements as long as the left pointer is less than the right pointer
    while left < right:
        # Swap the elements at the left and right positions simultaneously
        s[left], s[right] = s[right], s[left]
        # Move the left pointer one step towards the middle
        left += 1
        # Move the right pointer one step towards the middle
        right -= 1
