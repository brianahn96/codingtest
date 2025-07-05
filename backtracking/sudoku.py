# https://www.acmicpc.net/problem/2580

graph = []
blank = []

for i in range(9):
    graph.append(list(map(int, input().split(" "))))

for i in range(9):
    for j in range(9):
        if not graph[i][j]:
            blank.append([i, j])

def checkRow(x, value):
    for i in range(9):
        if graph[x][i] == value:
            return False
    return True

def checkCol(y, value):
    for i in range(9):
        if graph[i][y] == value:
            return False
    return True

def checkRect(x, y, value):
    dx = x // 3 * 3
    dy = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if graph[dx + i][dy + j] == value:
                return False
    return True

def dfs(index):
    if index == len(blank):
        for i in range(9):
            print(*graph[i])
        exit(0)

    for i in range(1, 10):
        x = blank[index][0]
        y = blank[index][1]
        
        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i):
            graph[x][y] = i
            dfs(index + 1)
            graph[x][y] = 0

dfs(0)