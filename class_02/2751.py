import sys
input = sys.stdin.readline

N = int(input())
list_num = []
for _ in range(N):
    list_num.append(int(input()))
list_num.sort()
for _ in range(N):
    print(list_num[_])

