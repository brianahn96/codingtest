# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

def minReorder(n: int, connections: list[list[int]]) -> int:
    adjacent = defaultdict(list)
    seen = set()
    for x, y in connections:
        adjacent[x].append(y)
        adjacent[y].append(x)
        seen.add((x, y))

    stack = [0]
    visited = set([0])
    ans = 0

    while stack:
        node = stack.pop()

        for end in adjacent[node]:
            if end not in visited:
                visited.add(end)
                if (node, end) in seen:
                    ans += 1
                stack.append(end)

    return ans

n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
print(minReorder(n, connections))