import sys

def ver_num(*args):
    num = 0
    for i in range(len(args[0])):
        num = num + (args[0][i] ** 2)
    return num % 10

Uni_num = list(map(int, sys.stdin.readline().split()))
print(ver_num(Uni_num))