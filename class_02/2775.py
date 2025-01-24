import sys

T = int(sys.stdin.readline())


def apart_resident(apart, k, n):
    # 0 층 주민 입실
    for i in range(n):
        apart[0][i] = i + 1
    # 각 층 1호 입실
    for i in range(k):
        apart[i][0] = 1

    # 각 층 주민 계산
    for i in range(1, k):
        for j in range(1, n):
            apart[i][j] = apart[i - 1][j] + apart[i][j - 1]
    return apart[k -1][n -1]


for _ in range(T):
    k = int(sys.stdin.readline()) + 1
    n = int(sys.stdin.readline())
    apart = [[0 for i in range(n)] for j in range(k)]

    print(apart_resident(apart, k, n))
