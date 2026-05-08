# Overall Time Complexity: O(N) where N is the length of the input string
# Overall Space Complexity: O(K) where K is the number of unique characters in the input string

# Given a string s, remove duplicate letters so that every letter appears once and only once. 
# You must make sure your result is the smallest in lexicographical order among all possible results.

# Example 1:

# Input: s = "bcabc"
# Output: "abc"

# Example 2:

# Input: s = "cbacdcbc"
# Output: "acdb"

# Define a function to remove duplicate letters and maintain smallest lexicographical order
def removeDuplicateLetters(s: str) -> str:
    # Create a dictionary to store the last occurrence index of each character in the string
    last = {char : i for i, char in enumerate(s)}
    # Initialize an empty stack to build the resulting string
    stack = []
    # Use a set to keep track of characters currently in the stack for efficient lookups
    seen = set()

    # Iterate through the string with both index and character
    for i, char in enumerate(s):
        # If the character is already in the stack, skip it to avoid duplicates
        if char in seen:
            # Continue to the next iteration of the for loop
            continue
        # While the stack is not empty and current char is smaller than the stack's top and the top char appears later
        while stack and char < stack[-1] and last[stack[-1]] > i:
            # Remove the top character from the seen set and the stack
            seen.remove(stack.pop())
        # Append the current character to the stack
        stack.append(char)
        # Add the current character to the seen set
        seen.add(char)
    
    # Join the characters in the stack to form the final string and return it
    return ''.join(stack)

# Define a sample input string for testing
s = "cbacdcbc"

# Call the function with the sample string (result not stored but processed)
removeDuplicateLetters(s)

# Create the last occurrence dictionary again for the sample string to demonstrate it
last = {char : i for i, char in enumerate(s)}
# Print the last occurrence dictionary to the console
print(last)
