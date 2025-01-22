import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

mul_num = A * B * C

for i in range(10):
    print(str(mul_num).count(f'{i}'))
