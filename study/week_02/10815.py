import sys

input = sys.stdin.readline

N = int(input())
num_list = set(map(int, input().split()))
M = int(input())
check_list = list(map(int, input().split()))
print_list = [0] * M


for i in range(M):
    if check_list[i] in num_list:
        print_list[i] = 1

print(" ".join(map(str, print_list)))
