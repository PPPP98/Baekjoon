import sys

T = int(sys.stdin.readline())

for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    num = (N // H) + 1
    floor = N % H
    if floor == 0:
        floor = H
        num -= 1
    if num < 10:
        print(f"{floor}0{num}")
    else:
        print(f"{floor}{num}")