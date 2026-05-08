# Time Complexity: O(S + T) where S is length of s, T is length of t (for optimized version)
# Space Complexity: O(1) - Hash maps store at most character set size
#
# https://leetcode.com/problems/minimum-window-substring/description/

# Time Overflow
def minWindow(s: str, t: str) -> str:
    answer = ""
    left = 0
    length = len(s)
    while left < length:
        if s[left] in list(t):
            t_list = list(t)
            right = left
            while right < length and t_list:
                if s[right] in t_list:
                    t_list.remove(s[right])
                    if not t_list:
                        answer = s[left:right + 1]
                        break
                right += 1
        left += 1
    print(answer)

from collections import Counter

def minWindow2(s: str, t: str) -> str:
    if not s or not t:
        return ""

    need = Counter(t)
    window = {}

    required = len(need)
    formed = 0

    left = 0
    res_len = float("inf")
    res = (0, 0)

    for right, char in enumerate(s):
        window[char] = window.get(char, 0) + 1

        if char in need and window[char] == need[char]:
            formed += 1
            
        while formed == required:
            if right - left + 1 < res_len:
                res_len = right - left + 1
                res = (left, right)
            
            left_char = s[left]
            window[left_char] -= 1
            
            if left_char in need and window[left_char] < need[left_char]:
                formed -= 1
                
            left += 1
            
    return "" if res_len == float("inf") else s[res[0]:res[1] + 1]
    

print(minWindow2("ADOBECODEBANC", "ABC"))