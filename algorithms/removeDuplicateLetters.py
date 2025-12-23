# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

# Example 1:

# Input: s = "bcabc"
# Output: "abc"

# Example 2:

# Input: s = "cbacdcbc"
# Output: "acdb"

def removeDuplicateLetters(s: str) -> str:
    last = {char : i for i, char in enumerate(s)}
    stack = []
    seen = set()

    for i, char in enumerate(s):
        if char in seen:
            continue
        while stack and char < stack[-1] and last[stack[-1]] > i:
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)
    
    return ''.join(stack)

s = "cbacdcbc"

removeDuplicateLetters(s)