# https://school.programmers.co.kr/learn/courses/30/lessons/258711

def solution(edges):
    answer = [0,0,0,0]
    
    startmap = dict()
    endmap = dict()
    
    for start, end in edges:
        if start not in startmap:
            startmap[start] = list()
        startmap[start].append(end)
        if end not in endmap:
            endmap[end] = list()
        endmap[end].append(start)
    
    point = 0
    
    for key in startmap.keys():
        if key not in endmap.keys() and len(startmap[key]) >= 2:
            point = key

    def check(start):
        if start not in startmap:
            return 2
        if len(startmap[start]) == 2:
            return 3
        index = startmap[start][0]
        while True:
            if index not in startmap:
                return 2
            if len(startmap[index]) == 2:
                return 3
            if index == start:
                return 1
            index = startmap[index][0]
    answer[0] = point
    for start in startmap[point]:
        answer[check(start)] += 1
    
    return answer