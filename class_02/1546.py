import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

Max = max(arr)
arr_new = list(map(lambda x: (x / Max) * 100, arr))
print(sum(arr_new) / N)
