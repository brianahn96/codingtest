# https://leetcode.com/problems/string-compression/description/?envType=study-plan-v2&envId=leetcode-75

def compress(chars: list[str]) -> int:
    ans = 0
    start = 0

    while start < len(chars):
        letter = chars[start]
        count = 0

        while start < len(chars) and chars[start] == letter:
            count += 1
            start += 1
        chars[ans] = letter
        ans += 1
        if count > 1:
            for c in str(count):
                chars[ans] = c
                ans += 1
    return ans