import sys

N = int(sys.stdin.readline())

N -= 1
i = 1
while N > 0:
    N = N - (6 * i)
    i += 1

print(i)
