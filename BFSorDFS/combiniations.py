# https://leetcode.com/problems/combinations/description/

def combine(n: int, k: int) -> list[list[int]]:
    results = []
    
    def dfs(elements, start: int, k: int):
        if k == 0:
            results.append(elements[:])
            
        for i in range(start, n + 1):
            elements.append(i)
            dfs(elements, i + 1, k - 1)
            elements.pop()
    
    dfs([], 1, k)
    return results