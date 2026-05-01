# https://leetcode.com/problems/different-ways-to-add-parentheses/description/

def diffWaysToCompute(expression: str) -> list[int]:
    
    def compute(left, op, right):
        values = []
        
        for l in left:
            for r in right:
                values.append(eval(str(l) + op + str(r)))
        
        return values
    
    results = []
    
    if expression.isdigit():
        return [int(expression)]
    
    for index, value in enumerate(expression):
        if value in "-+*":
            left = diffWaysToCompute(expression[:index])
            right = diffWaysToCompute(expression[index + 1:])
            
            results.extend(compute(left, value, right))
    
    return results
    
expression = "2*3-4*5"

print(diffWaysToCompute(expression))