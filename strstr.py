# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

def strStr(haystack: str, needle: str) -> int:
    len_needle = len(needle)

    for i in range(len(haystack) - len_needle + 1):
        if haystack[i:i+len_needle] == needle:
            return i
    return -1