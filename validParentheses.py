# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true

# Example 2:

# Input: s = "()[]{}"
# Output: true

# Example 3:

# Input: s = "(]"
# Output: false

def validParentheses(s: str) -> bool:
    parentheses = {")" : "(", "]" : "[", "}" : "{"}
    
    stack = []
    
    for char in s:
        if char not in parentheses:
            stack.append(char)
        elif not stack or parentheses[char] != stack.pop():
            return False
        
    return len(stack) == 0