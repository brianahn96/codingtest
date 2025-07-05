# https://www.acmicpc.net/problem/1912

N = int(input())
arrays = list(map(int, input().split(" ")))

for i in range(1, N):
    arrays[i] = max(arrays[i], arrays[i - 1] + arrays[i])
    
print(max(arrays))