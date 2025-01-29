import sys

input = sys.stdin.readline
N = input()

arr_N = set(map(int, input().split()))

M = input()
arr_M = list(map(int, input().split()))

for num in arr_M:
    if num in arr_N:
        sys.stdout.write('1\n')
    else:
        print(0)
