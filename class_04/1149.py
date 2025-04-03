import sys

input = lambda: sys.stdin.readline().strip()

N = int(input())
cost = [tuple(map(int, input().split())) for _ in range(N)]

memo = [[0, 0, 0] for _ in range(N + 1)]


def cal(i, j):
    temp = []
    for k in range(3):
        if j != k:
            temp.append(memo[i][k] + cost[i][j])
    return min(temp)


for i in range(1, N + 1):
    for j in range(3):
        memo[i][j] = cal(i - 1, j)

print(min(memo[N]))
