# https://leetcode.com/problems/decode-string/description/

def decodeString(s: str) -> str:
    stack = []

    for char in s:
        stack.append(char)

        if stack[-1] == "]":
                res = ""
                count = ""
                while stack and stack[-1] != "[":
                    ele = stack.pop()
                    if ele.isalpha():
                        res = ele + res
                stack.pop()
                while stack and stack[-1].isdigit():
                    ele = stack.pop()
                    count = ele + count
                stack.extend([ele for ele in res] * int(count))
                
    return "".join(stack)