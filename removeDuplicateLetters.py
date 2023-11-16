# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
# the smallest in lexicographical order
#  among all possible results.

 

# Example 1:

# Input: s = "bcabc"
# Output: "abc"
# Example 2:

# Input: s = "cbacdcbc"
# Output: "acdb"

from collections import Counter

def removeDuplicateLetters(s: str) -> str:
    counter, stack = Counter(s), []
    
    for char in s:
        counter[char] -= 1
        if char in stack:
            continue
        while stack and stack[-1] and counter[stack[-1]] > 0:
            stack.pop()
        stack.append(char)
    
    return ''.join(stack)