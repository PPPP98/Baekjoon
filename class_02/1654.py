import sys

input = sys.stdin.readline

N, K = map(int, input().split())  # K <= N

sum_len = 0
rope = []
for _ in range(N):
    num = int(input())
    sum_len += num
    rope.append(num)


# K * target + C = sum
high = sum_len // K
low = 1
result = 0
while low <= high:
    target = (high + low) // 2

    remain = 0
    for num in rope:
        remain += num % target

    if sum_len < ((K * target) + remain):
        high = target - 1
    else:
        low = target + 1

print(high)
