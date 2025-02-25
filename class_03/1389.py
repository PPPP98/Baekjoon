import sys

input = sys.stdin.readline


N, M = map(int, input().split())

friend = [[float("inf")] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    friend[i][i] = 0
    friend[i][0] = 0

for _ in range(M):
    v, e = map(int, input().split())
    friend[v][e] = 1
    friend[e][v] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            friend[i][j] = min(friend[i][j], friend[i][k] + friend[k][j])


min_v = float("inf")
min_idx = 0
for i in range(1, N + 1):
    sum_re = sum(friend[i])
    if min_v > sum_re:
        min_v = sum_re
        min_idx = i

print(min_idx)
