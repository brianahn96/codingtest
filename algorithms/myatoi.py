# https://leetcode.com/problems/string-to-integer-atoi/

def myAtoi(s: str) -> int:
    res = 0
    is_negative = False
    reading_start = False
    for char in s:
        if not reading_start:
            if char == " ": continue
            if char == "-" :
                reading_start = True
                is_negative = True
                continue
            if char == "+" :
                reading_start = True
                is_negative = False
                continue
        if char.isnumeric():
            reading_start = True
            res = res*10 + int(char)
        else: break

    if is_negative:
        res = res *-1

    minimum, maximum = -1 * 2**31, 2**31 - 1
    if res < minimum:
        return minimum
    elif res > maximum:
        return maximum
    else:
        return res