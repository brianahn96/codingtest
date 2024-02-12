# https://www.acmicpc.net/problem/14888

N = int(input())
numbers = list(map(int, input().split(" ")))
operations = list(map(int, input().split(" ")))
maximum, minimum = -1000000000, 1000000000
        
def backtracking(n, val):
    global maximum, minimum
    
    def operate(index, operand, value):
        if index == 0:
            return operand + value
        elif index == 1:
            return operand - value
        elif index == 2:
            return operand * value
        elif index == 3:
            if operand < 0:
                return -1 * ((-1 * operand) // value)
            else:
                return operand // value
                
    if n == N:
        maximum = max(maximum, val)
        minimum = min(minimum, val)
        return
    
    for index, i in enumerate(operations):
        if i:
            operated = operate(index, val, numbers[n])
            operations[index] -= 1
            backtracking(n + 1, operated)
            operations[index] += 1
            
backtracking(1, numbers[0])
print(maximum)
print(minimum)