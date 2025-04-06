import sys

input = lambda:sys.stdin.readline().strip()

N = int(input())

triangle = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * i for i in range(1, N + 1)]

dp[0][0] = triangle[0][0]

for i in range(1, N):

    for j in range(i + 1):
        t1 = dp[i - 1][j - 1] + triangle[i][j] if 0 <= (j - 1) else 0
        t2 = dp[i - 1][j] + triangle[i][j] if  j < i else 0


        dp[i][j] = max(t1, t2)

print(max(dp[N - 1]))