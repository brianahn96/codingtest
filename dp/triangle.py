# https://www.acmicpc.net/problem/1932

N = int(input())
triangle = []

for i in range(N):
    triangle.append(list(map(int, input().split(" "))))
    
for i in range(1, N):
    length = len(triangle[i])
    for j in range(length):
        if j == 0:
            triangle[i][j] += triangle[i - 1][j]
        elif j == length - 1:
            triangle[i][j] += triangle[i - 1][-1]
        else:
            triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
            
print(max(triangle[N - 1]))