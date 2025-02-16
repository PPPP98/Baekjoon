N = int(input())

dp = [0, 1, 2, 3, 5]

for i in range(5, N + 1):
    dp.append(dp[i - 1] + dp[i - 2])

print(dp[N] % 10007)