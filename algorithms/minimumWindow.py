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
    

minWindow("ADOBECODEBANC", "ABC")
