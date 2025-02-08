import sys
input = sys.stdin.readline
print = sys.stdout.write

name_dict = {}
num_dict = {}

N, M = map(int, input().split())

for i in range(1, N + 1):
    name = input().strip()
    name_dict[name] = i
    num_dict[i] = name

for _ in range(M):
    info = input().strip()
    if info.isdecimal():
        print(f"{num_dict[int(info)]}\n")
    else:
        print(f"{name_dict[info]}\n")
