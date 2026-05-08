# Overall Time Complexity: O(3^N * 4^M) where N is number of 3-letter digits and M is number of 4-letter digits
# Overall Space Complexity: O(N + M) for recursion stack depth
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
# Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Example 2:

# Input: digits = ""
# Output: []

# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]

# Import List for type hinting
from typing import List

# Define the letterCombinations function
def letterCombinations(digits: str) -> List[str]:
    # Check if the input digits string is empty
    if not digits:
        # If empty, return an empty list
        return []
    
    # Define a dictionary mapping digits to their corresponding letters
    dic = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
    
    # Initialize a list to store the final combinations
    results = []
    
    # Define the depth-first search helper function
    def dfs(index, path):
        
        # Check if the length of the current path equals the length of input digits
        if len(path) == len(digits):
            # If so, a complete combination is formed, add it to results
            results.append(path)
            # Return to continue searching
            return
        
        # Iterate through the digits starting from the current index
        for i in range(index, len(digits)):
            # Iterate through each letter corresponding to the current digit
            for letter in dic[digits[i]]:
                # Recurse with the next digit index and updated path
                dfs(i + 1, path + letter)
                
    # Initial call to dfs starting at index 0 with an empty path
    dfs(0, "")
    
    # Return the final results list
    return results

# Define a test string of digits
digits = "23"
# Print the results of letterCombinations for the test string
print(letterCombinations(digits))
