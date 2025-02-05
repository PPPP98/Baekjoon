import sys
import math
input = sys.stdin.readline
print = sys.stdout.write

M, N = map(int, input().split())

prime_arr = [False,False] + [True]*(N-1)
prime_num = []

for i in range(2, N + 1):
    if prime_arr[i]:
        if i >= M:
            prime_num.append(i)
        for j in range(2*i, N + 1, i):
            prime_arr[j] = False

for num in prime_num:
    print(f"{num}\n")



