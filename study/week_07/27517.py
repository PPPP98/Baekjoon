<<<<<<< HEAD
import sys

input = lambda:sys.stdin.readline().strip()

N = int(input())
arr = list(map(int, input().split()))

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
