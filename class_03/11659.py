import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(1, N):
    arr[i] += arr[i - 1]

for i in range(M):
    A, B = map(int, input().split())
    if A == 1:
        print(arr[B - 1])
        continue
    print(arr[B - 1] - arr[A - 2])



