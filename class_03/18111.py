import sys

input = sys.stdin.readline

N, M, B = map(int, input().split())

min_h = float("inf")
max_h = float("-inf")

height_list = [0] * 257
total = 0

for _ in range(N):
    arr = list(map(int, input().split()))
    for h in arr:
        min_h = min(min_h, h)
        max_h = max(max_h, h)
        total += h
        height_list[h] += 1

result = float("inf")
result_h = 0


if max_h > (total + B) // (N * M):
    max_h = (total + B) // (N * M)


for h in range(min_h, max_h + 1):
    time = 0

    for i in range(257):
        if i > h:
            time += ((i - h) * height_list[i]) * 2
        elif i < h:
            time += (h - i) * height_list[i]

    if result >= time:
        result = time
        result_h = h

print(result, result_h)
