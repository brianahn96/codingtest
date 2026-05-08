# Overall Time Complexity: O(S * N) where S is the length of the shortest string and N is the number of strings
# Overall Space Complexity: O(N) due to the set used to store characters at each index

# Import List from typing for type annotation support
from typing import List

# Link to the problem on LeetCode
# https://leetcode.com/problems/longest-common-prefix/

# Define a function that takes a list of strings and returns their longest common prefix
def longestCommonPrefix(strs: List[str]) -> str:
    # Initialize an empty string to accumulate the common prefix
    res = ""
    # Calculate the minimum length among all strings to avoid index out of bounds
    min_length = min([len(x) for x in strs])

    # Iterate through indices from 0 up to the minimum string length
    for i in range(min_length):
        # Create a set to collect the character at index i from each string
        letter = set()
        # Loop through each individual string in the input list
        for word in strs:
            # Add the character at the current index i of the current word to the set
            letter.add(word[i])
        # If the set has more than one unique character, the common prefix ends
        if len(letter) != 1:
            # Terminate the loop as the characters at this index do not match across all strings
            break
        # Append the single unique character found in the set to the result string
        res += letter.pop()
        
    # Return the accumulated longest common prefix string
    return res
