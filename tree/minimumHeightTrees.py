# https://leetcode.com/problems/minimum-height-trees/description/

from collections import defaultdict

def findMinHeightTrees(n: int, edges: list[list[int]]) -> list[int]:
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        
    print(graph)
    
    leaves = []
    for i in range(n):
        if len(graph[i]) == 1:
            leaves.append(i)
            
    print(leaves)
    
    while n > 2:
        n -= len(leaves)
        new_leaves = []
        for leaf in leaves:
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)
            
            if len(graph[neighbor]) == 1:
                new_leaves.append(neighbor)
                
        leaves = new_leaves
    
    return leaves
    
n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]

n = 4
edges = [[1,0],[1,2],[1,3]]

print(findMinHeightTrees(n, edges))
