import sys

input = sys.stdin.readline
# N 세로 M 가로
N, M = map(int, input().split())
# 체스판 입력
field_chess = [list(input().strip()) for _ in range(N)]

change_count_list_W = [[0 for _ in range(M - 7)] for _ in range(N)]
change_count_list_B = [[0 for _ in range(M - 7)] for _ in range(N)]


def change_count(arr, flag):
    count = 0
    for i in arr:
        if flag:
            if i != "W":
                count += 1
            flag = False
        else:
            if i != "B":
                count += 1
            flag = True
    return count


# 첫 타일 흑 백 구분분
flag_W = True  # 백

flag_B = False # 흑

for j in range(M - 7):
    for i in range(N):
        temp = field_chess[i][j : j + 8]
        if flag_W:
            change_count_list_W[i][j] = change_count(temp, flag_W)
            flag_W = False
        else:
            change_count_list_W[i][j] = change_count(temp, flag_W)
            flag_W = True
        if flag_B:
            change_count_list_B[i][j] = change_count(temp, flag_B)
            flag_B = False
        else:
            change_count_list_B[i][j] = change_count(temp, flag_B)
            flag_B = True
    if N % 2 == 0:
        if flag_W:
            flag_W = False
        else:
            flag_W = True
        if flag_B:
            flag_B = False
        else:
            flag_B = True


min_change = 65
for j in range(M - 7): # 0 <= ~ < 6      0, 1, 2, 3, 4, 5
    for i in range(N - 7): # 0 <= x < 3    0, 1, 2
        temp_W = 0
        temp_B = 0
        for k in range(8): # 0 ~ 7
            temp_W += change_count_list_W[i + k][j]
            temp_B += change_count_list_B[i + k][j]
        if temp_W < temp_B:
            if temp_W < min_change:
                min_change = temp_W
        else:
            if temp_B < min_change:
                min_change = temp_B

print(min_change)
