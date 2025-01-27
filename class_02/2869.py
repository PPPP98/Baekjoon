import sys

A, B, V = map(int, sys.stdin.readline().split())
# (V - A) / (A - B)

N1 = V - A
N2 = A - B

if N1 % N2 == 0:
    print(int(N1 / N2) + 1)
else:
    print(int(N1 / N2) + 2)
