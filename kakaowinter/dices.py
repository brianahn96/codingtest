# https://school.programmers.co.kr/learn/courses/30/lessons/258709

def solution(dice):
    answer = []
    maximum = 0
    trueanswer = []
    length = len(dice)
    base = list(range(length))
    
    def backtracking(index, path):
        if len(path) == length // 2:
            answer.append(path[:])
        for i in range(index, length):
            path.append(i)
            backtracking(i + 1, path)
            path.pop()
    
    backtracking(0, [])

    def calculateprob(comb):
        windict = {}
        def backtrackingcal(index, summed):
            if len(summed) == len(comb):
                total = sum(summed)
                if total not in windict:
                    windict[total] = 1
                else:
                    windict[total] += 1
                return
            for i in range(6):
                summed.append(dice[comb[index]][i])
                backtrackingcal(index + 1, summed)
                summed.pop()
        backtrackingcal(0, [])
        return windict
    
    combinationdict = {}
    for i in range(len(answer)):
        combinationdict[i] = calculateprob(answer[i])

    for i in range(len(combinationdict) // 2):
        first = last = 0
        for value, count in combinationdict[i].items():
            for value2, count2 in combinationdict[len(combinationdict) - i - 1].items():
                if value > value2:
                    first += count * count2
                elif value < value2:
                    last += count2 * count
        bigger = i if first > last else len(combinationdict) - i - 1
        if first > maximum:
            maximum = first
            trueanswer = answer[i]
        if last > maximum:
            maximum = last
            trueanswer = answer[len(combinationdict) - i - 1]
    return [x + 1 for x in trueanswer]