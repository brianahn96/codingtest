# https://school.programmers.co.kr/learn/courses/30/lessons/154540

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(i):
        stack = []
        stack.append(i)
        
        while stack:
            last = stack.pop()
            visited[last] = True
            for idx, node in enumerate(computers[last]):
                if not visited[idx] and node:
                    stack.append(idx)
        
    for node in range(n):
        if not visited[node]:
            dfs(node)
            answer += 1
    return answer