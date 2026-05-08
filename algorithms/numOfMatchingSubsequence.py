# Time Complexity: O(S + W * L * log(S)) where S is length of s, W is number of words, L is average word length
# Space Complexity: O(S) for storing character positions in the dictionary
#
# https://leetcode.com/problems/number-of-matching-subsequences/description/

from collections import defaultdict

def numMatchingSubseq(s: str, words: list[str]) -> int:
    ans = 0
    letter_positions = defaultdict(list)
    for i, c in enumerate(s):
        letter_positions[c].append(i)
    
    def upper_bound(arr, target):
        left, right = 0, len(arr)
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left
    
    def is_subsequence(word):
        curr_pos = -1
        for letter in word:
            if letter not in letter_positions:
                return False
            
            indices = letter_positions[letter]
            idx = upper_bound(indices, curr_pos)
            
            if idx == len(indices):
                return False
            curr_pos = indices[idx]
        return True
    
    for word in words:
        if is_subsequence(word):
            ans += 1
            
    return ans
    
s = "abcde"
words = ["a","bb","acd","ace"]

s = "dsahjpjauf"
words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]

print(numMatchingSubseq2(s, words))