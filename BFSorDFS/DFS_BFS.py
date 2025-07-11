graph = {
    1:[2,3,4],
    2:[5],
    3:[5],
    4:[],
    5:[6,7],
    6:[],
    7:[3]
}

# Implementing DFS with recursion
def recursive_dfs(graph, v, discovered = []):
    discovered.append(v)
    for w in graph[v]:
        if not w in discovered:
            discovered = recursive_dfs(graph, w, discovered)
    return discovered

# Implementing DFS with stack
def iterative_dfs(graph, start_v):
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered

# Implementing BFS with queue
def iterative_bfs(graph, start_v):
    discovered = [start_v]
    queue = [start_v]
    
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered