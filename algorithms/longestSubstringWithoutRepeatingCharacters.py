# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

def lengthOfLongestSubstring(s: str) -> int:
    start = 0
    length = 0

    while start < len(s):
        seen = set()
        seen.add(s[start])
        index = start + 1
        while index < len(s) and s[index] not in seen:
            seen.add(s[index])
            index += 1
        length = max(length, index - start)
        if index == len(s):
            break
        start += 1
    
    return length

def lengthOfLongestSubstringSlidingWindow(s: str) -> int:
    left = max_length = 0
    char_set = set()
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length