N = int(input())

dp = [0, 1, 3, 5]

for i in range(4, N + 1):
    dp.append(dp[i - 1] + 2 * dp[i - 2])

print(dp[N] % 10007)