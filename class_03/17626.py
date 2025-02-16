N = int(input())

max_num = int(N ** 0.5)

dp = [0, 1, 2]

for i in range(3, N + 1):
    min_v = float('inf')
    for j in range(1, max_num + 1):
        square = (j ** 2)
        if square <= i:
            min_v = min(min_v, (1 + dp[i - square]))
        else:
            break
    dp.append(min_v)

print(dp[N])