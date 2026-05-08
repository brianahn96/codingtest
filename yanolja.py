from collections import deque

def func(maze):
    # Time Complexity: O(N*M) where N is rows, M is columns (BFS)
    # Space Complexity: O(N*M) for visited set and queue
    n, m = len(maze), len(maze[0])
    directions = [(0,1),(0,-1),(1,0),(-1,0)]

    # start, end 찾기
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 2:
                sx, sy = i, j
            elif maze[i][j] == 3:
                ex, ey = i, j

    queue = deque([(sx, sy, 0)])
    visited = set([(sx, sy)])

    while queue:
        x, y, dist = queue.popleft()

        if (x, y) == (ex, ey):
            return dist

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] != 1 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, dist + 1))

    return -1  # 도착 불가

# Test Case 1: Basic 3x3 maze with clear path
test_maze1 = [
    [2, 0, 0],
    [0, 1, 0],
    [0, 0, 3]
]
# Expected: 4 (right, right, down, down)
# Test Case 2: No path to destination
test_maze2 = [
    [2, 1, 0],
    [1, 1, 0],
    [0, 0, 3]
]
# Expected: -1 (blocked by walls)
# Test Case 3: Larger 5x5 maze
test_maze3 = [
    [2, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 2, 0, 0],
    [0, 1, 0, 1, 1],
    [0, 0, 0, 0, 3]
]
# Expected: 8 (needs to go around walls)
# Test Case 4: Start and end are adjacent
test_maze4 = [
    [2, 3],
    [0, 0]
]
# Expected: 1
# Test Case 5: Single cell maze (just start and end)
test_maze5 = [
    [2, 3]
]
# Expected: 1
# Test Case 6: Large open space
test_maze6 = [
    [2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 3]
]
# Expected: 8 (diagonal path)
# Test Case 7: Maze with multiple paths
test_maze7 = [
    [2, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 3]
]
# print(func(test_maze3))


def find_expressions_to_100():
    # Time Complexity: O(3^N) where N=9 (number of digit gaps)
    # Space Complexity: O(N) for recursion stack depth
    
    digits = "123456789"
    results = []

    def dfs(index: int, expr: str):
        # Time Complexity: O(3^N) for exploring all operator combinations
        # Space Complexity: O(N) for recursion stack
        if index == len(digits):
            if eval(expr) == 100:
                results.append(expr)
            return

        # 1) + 연산자
        dfs(index + 1, expr + "+" + digits[index])

        # 2) - 연산자
        dfs(index + 1, expr + "-" + digits[index])

        # 3) 숫자 이어붙이기
        dfs(index + 1, expr + digits[index])

    # 시작은 반드시 '1'
    dfs(1, digits[0])
    return results


answers = find_expressions_to_100()

def plusOne(digits: list[int]) -> list[int]:
    # Time Complexity: O(N) where N is number of digits (worst case all 9s)
    # Space Complexity: O(1) if not counting output, O(N) if carry creates new digit
    carry, i = 0, len(digits) - 1

    while i > -1:
        summed = digits[i] + 1
        if summed == 10:
            digits[i] = 0
            carry = 1
            i -= 1
        else:
            digits[i] = summed
            return digits

    if carry:
        digits.insert(0, carry)
        return digits
    
digits = [9]
print(plusOne(digits))