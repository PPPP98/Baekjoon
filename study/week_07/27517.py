import sys

input = lambda:sys.stdin.readline().strip()

N = int(input())
arr = list(map(int, input().split()))

s_arr = sorted(arr)
res = 0
for i in range(len(arr)):
    res += (arr[i] - s_arr[i]) * (N - i + 1)

print(res % 1000000007)