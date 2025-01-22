import sys

H, M = map(int, sys.stdin.readline().split())

M_H = 0
M_M = 0
#1 분에서 빼기
if (M - 45) >= 0:
    M_M = M - 45
    M_H = H
else:
    M_M = 60 + M - 45
    if (H - 1) >= 0:
        M_H = H - 1
    else:
        M_H = 23

print(f'{M_H} {M_M}')