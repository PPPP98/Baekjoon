import sys

input = lambda: sys.stdin.readline().strip()

out = lambda x: sys.stdout.write(x + "\n")


N, M = map(int, input().split())

dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    arr = list(map(int, input().split()))
    for j in range(1, N + 1):
        dp[i][j] = dp[i][j - 1] + arr[j - 1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    res = 0
    for i in range(x1, (x2 + 1)):
        res += dp[i][y2] - dp[i][y1 - 1]
    out(str(res))
