# https://leetcode.com/problems/number-of-provinces/description/

from collections import deque

def findCircleNum(isConnected: list[list[int]]) -> int:
    ans = 0
    visited = set()

    def dfs(index):
        stack = [index]
        visited.add(index)

        while stack:
            vertex = stack.pop()
            for neighbor in range(len(isConnected)):
                if neighbor not in visited and isConnected[vertex][neighbor] == 1:
                    visited.add(neighbor)
                    stack.append(neighbor)


    for i in range(len(isConnected)):
        if i not in visited:
            dfs(i)
            ans += 1
    return ans