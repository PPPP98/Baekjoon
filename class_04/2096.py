import sys

input = lambda: sys.stdin.readline().strip()

N = int(input())

min_data = [0] * 3
next_min = [0] * 3
max_data = [0] * 3
next_max = [0] * 3

for i in range(N):
    a, b, c = map(int, input().split())
    for j in range(3):
        if j == 0:
            next_min[j] = min(min_data[j], min_data[j + 1]) + a
            next_max[j] = max(max_data[j], max_data[j + 1]) + a
        elif j == 1:
            next_min[j] = min(min_data[j], min_data[j + 1], min_data[j - 1]) + b
            next_max[j] = max(max_data[j], max_data[j + 1], max_data[j - 1]) + b
        elif j == 2:
            next_min[j] = min(min_data[j], min_data[j - 1]) + c
            next_max[j] = max(max_data[j], max_data[j - 1]) + c

    for j in range(3):
        min_data[j] = next_min[j]
        max_data[j] = next_max[j]
        next_min[j], next_max[j] = 0, 0


print(max(max_data), min(min_data))
