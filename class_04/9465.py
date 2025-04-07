import sys

input = lambda: sys.stdin.readline().strip()

T = int(input())

for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * (N + 1) for _ in range(2)]

    dp[0][1], dp[1][1] = arr[0][0], arr[1][0]

    for i in range(2, N + 1):

        for j in range(2):
            dp[j][i] = max(
                (dp[j ^ 1][i - 2] + arr[j][i - 1]), (dp[j ^ 1][i - 1] + arr[j][i - 1])
            )

    print(max(dp[0][N], dp[1][N]))
