import sys
input = sys.stdin.readline
print = sys.stdout.write

N_list = [0 for i in range(10001)]
N = int(input())

for i in range(N):
    N_list[int(input()) - 1] += 1

for i in range(10001):
    if N_list[i] != 0:
        for j in range(N_list[i]):
            print(f"{i + 1}\n")
