# https://leetcode.com/problems/evaluate-division/description/

from collections import defaultdict, deque

def calcEquationDFS(equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
    mult = defaultdict(dict)

    for index,  (up, down) in enumerate(equations):
            mult[up][down] = values[index]
            mult[down][up] = 1 / values[index]
    print(mult)
    def dfs(start, end, visited):
        if start not in mult or end not in mult:
            return -1.0
        if start == end:
            return 1.0
        visited.add(start)

        for neighbor, val in mult[start].items():
            if neighbor not in visited:
                result = dfs(neighbor, end, visited)
                if result != -1.0:
                    return result * val
        return -1.0

    return [dfs(a, b, set()) for a, b in queries]

def calcEquationBFS(equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
    mult = defaultdict(dict)
    
    for index,  (up, down) in enumerate(equations):
            mult[up][down] = values[index]
            mult[down][up] = 1 / values[index]

    def bfs(start,end):
        if start not in mult or end not in mult:
            return -1.0
        
        if start == end:
            return 1.0
        
        queue = deque([(start,1.0)])
        visited = {start}
        
        while queue:
            node, curr = queue.popleft()
            
            for neighbor, value in mult[node].items():
                if neighbor in visited:
                    continue
                
                result = curr * value
                
                if neighbor == end:
                    return result
                
                mult[start][neighbor] = result
                mult[neighbor][start] = 1 / result
                
                visited.add(neighbor)
                queue.append((neighbor,result))
                
        return -1.0
    
    return [bfs(start,end) for start,end in queries]


equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

equations = [["a","b"],["b","c"],["bc","cd"]]
values = [1.5,2.5,5.0]
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]

print(calcEquationDFS(equations, values, queries))