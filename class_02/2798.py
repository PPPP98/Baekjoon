import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))


max = 0

for i in range(N):
    for j in range(1 + i, N):
        for k in range(1 + j, N):
            sum = arr[i] + arr[j] + arr[k]
            if sum == M:
                max = sum
            elif max < sum < M:
                max = sum

print(max)
