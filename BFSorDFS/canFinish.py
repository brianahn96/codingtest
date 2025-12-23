# https://leetcode.com/problems/course-schedule/

from collections import defaultdict

def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:

    graph = defaultdict(list)

    for x, y in prerequisites:
        graph[x].append(y)

    traced = set()
    visited = set()

    def dfs(i):
        if i in traced:
            return False

        if i in visited:
            return True

        traced.add(i)

        for y in graph[i]:
            if not dfs(y):
                return False

        traced.remove(i)
        visited.add(i)

        return True

    for x in list(graph):
        if not dfs(x):
            return False

    return True