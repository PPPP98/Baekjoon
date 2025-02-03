import sys

input = sys.stdin.readline
level = 30
# 계수정렬 난이도 별 카운트
level_list = [0 for _ in range(level)]

def round(N):
    if N - int(N) >= 0.5:
        return int(N) + 1
    else:
        return int(N)

N = int(input())  # 의견의 개수
excp_N = int(round(N * 0.15))  # 제외 인원

if N == 0 or round(N - (excp_N * 2)) == 0:
    print(0)
else:
    # 난이도 입력
    for _ in range(N):
        num = int(input())
        level_list[num - 1] += 1

    count = excp_N
    for i in range(level):
        if level_list[i] != 0:
            if count <= level_list[i]:
                level_list[i] -= count
                break
            else:
                count -= level_list[i]
                level_list[i] = 0

    count = excp_N
    for i in range(level - 1, -1, -1):
        if level_list[i] != 0:
            if count <= level_list[i]:
                level_list[i] -= count
                break
            else:
                count -= level_list[i]
                level_list[i] = 0

    result = 0
    for i in range(level):
        if level_list[i] != 0:
            result += (i + 1) * level_list[i]


    result /= N - (excp_N * 2)
    print(int(round(result)))

