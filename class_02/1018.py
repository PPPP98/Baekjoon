import sys

input = sys.stdin.readline

M, N = map(int, input().split())
# 체스판 입력
field_chess = [list(input().strip()) for _ in range(M)]

print(field_chess)