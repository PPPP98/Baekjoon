import sys

N = int(sys.stdin.readline())

num = 666
count = 1

if N == 1:
    print(num)
else:
    num = 1666
    while count != N:
        if '666' in str(num):
            count += 1
        num += 1

    print(num - 1)

