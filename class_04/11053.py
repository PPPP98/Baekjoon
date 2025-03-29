N = int(input())
arr = list(map(int, input().split()))
dp = [0] * N
dp[0] = 1

for i in range(1, N):
    max_v = 0
    for j in range(i):
        if arr[i] > arr[j]:
            max_v = max(max_v, dp[j])
    dp[i] = max_v + 1

res = max(dp)
print(res)
