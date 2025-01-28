import sys

input = sys.stdin.readline

N = int(input())

list_w_h = [[0 for _ in range(2)] for _ in range(N)]

for i in range(N):
    list_w_h[i][0], list_w_h[i][1] = map(int, input().split())


list_count = []
for i in range(N):
    count = 0
    for j in range(N):
        if list_w_h[i][0] < list_w_h[j][0]:
            if list_w_h[i][1] < list_w_h[j][1]:
                count += 1
    list_count.append(str(count + 1))


print(' '.join(list_count))