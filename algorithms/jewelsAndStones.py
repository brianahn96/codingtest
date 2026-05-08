# Time Complexity: O(J + S) where J is length of jewels, S is length of stones
# Space Complexity: O(J) for the frequency map
#
# https://leetcode.com/problems/jewels-and-stones/description/

def numJewelsInStones(jewels: str, stones: str) -> int:
    freqs = {}
    count = 0
    
    for char in jewels:
        freqs[char] = freqs.get(char, 0) + 1
    
    for char in stones:
        if char in freqs:
            count += 1
    
    return count