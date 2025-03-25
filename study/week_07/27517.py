<<<<<<< HEAD
<<<<<<< HEAD
import sys

input = lambda:sys.stdin.readline().strip()
=======
import sys

input = lambda: sys.stdin.readline().strip()
>>>>>>> e284b74 (25)

N = int(input())
arr = list(map(int, input().split()))

<<<<<<< HEAD
sort_arr = sorted(arr)
res = 0

for i in range(N - 1, -1, -1):
    target = sort_arr[i]
    j = 0
    now = 0
    while now != target:
        if now < arr[i - j]:
            remain = arr[i - j] - now
            now += remain
            arr[i - j] -= remain
            res += (j * remain)
        j += 1

print(res)
=======
>>>>>>> 42c7a81 (21)
=======
s_arr = sorted(arr)
res = 0
for i in range(len(arr) // 2):
    res += ((arr[i] - s_arr[i]) * (N - i - 1)) + ((arr[N - 1 - i] - s_arr[N - 1 - i]) * (i))

if N % 2 == 1:
    res += (arr[N // 2] - s_arr[N // 2]) * (N // 2)

print(res % 1000000007)
>>>>>>> e284b74 (25)
