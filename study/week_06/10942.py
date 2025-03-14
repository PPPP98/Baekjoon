import sys

input = lambda:sys.stdin.readline().strip()
print = lambda x:sys.stdout.write(x)


N = int(input())
arr = tuple(map(int, input().split()))

dp = [[0] * N for _ in range(N)]

for i in range(N):
    dp[i][i] = 1




M = int(input())
for _ in range(M):
