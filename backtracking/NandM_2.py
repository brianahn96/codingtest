# https://www.acmicpc.net/problem/15650

N, M = map(int, input().split())

s = []
def backtracking(index):
    """
    Time Complexity: O(C(N, M) * M) where C(N, M) = N! / (M!(N-M)!)
    Space Complexity: O(M) for the recursion stack and state list.
    """
    if len(s) == M:
        print(" ".join(map(str, s)))
        return
    for i in range(index, N + 1):
        s.append(i)
        backtracking(i + 1)
        s.pop()
        
backtracking(1)