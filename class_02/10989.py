import sys

N_list = [0 for i in range(10001)]
N = int(sys.stdin.readline().strip())

for i in range(N):
    N_list[int(sys.stdin.readline()) - 1] += 1

for i in range(10001):
    if N_list[i] != 0:
        for j in range(N_list[i]):
            print(i + 1)
