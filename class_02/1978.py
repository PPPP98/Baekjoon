N = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in range(N):
    if arr[i] < 2:
        cnt += 1
        continue
    else:
        for j in range(2, (int(arr[i] ** 0.5) + 1)):
            if arr[i] % j == 0:
                cnt += 1
                break

print(N - cnt)

