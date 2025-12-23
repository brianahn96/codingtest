# https://leetcode.com/problems/longest-common-prefix/

def longestCommonPrefix(strs: List[str]) -> str:
    res = ""
    min_length = min([len(x) for x in strs])

    for i in range(min_length):
        letter = set()
        for word in strs:
            letter.add(word[i])
        if len(letter) != 1:
            break
        res += letter.pop()
        
    return res