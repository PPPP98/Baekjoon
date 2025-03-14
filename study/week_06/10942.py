import sys

input = lambda:sys.stdin.readline().strip()
# print = lambda x:sys.stdout.write(x)


def check(s, e):
    if dp[s][e]:
        return check[s - 1][e - 1]
    else:
        return 0

N = int(input())
arr = tuple(map(int, input().split()))

dp = [[0] * N for _ in range(N)]


for i in range(N - 1 , -1, -1):
    for j in range(i, -1, -1):
        if arr[j] != arr[i]:
            continue
        else:
            




print(dp)



# M = int(input())

# for _ in range(M):
#     s, e = map(int, input().split())
#     if dp[s - 1][e - 1]:
#         print(1)
#     else:
#         print(0)
