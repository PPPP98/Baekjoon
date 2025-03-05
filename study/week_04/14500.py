import sys

input = sys.stdin.readline

"""
정사각형은 서로 겹치면 안 된다.
도형은 모두 연결되어 있어야 한다.
정사각형의 변끼리 연결되어 있어야 한다. 즉, 꼭짓점과 꼭짓점만 맞닿아 있으면 안 된다.
"""

di = (-1, 0, 1, 0)
dj = (0, 1, 0, -1)


def put_block(matrix, pos, d=-1, res=0, step=1):
    global max_v, max_point
    res += matrix[pos[0]][pos[1]]

    if res + max_point * (4 - step) <= max_v:
        return

    if step == 4:
        max_v = max(max_v, res)
        return

    for k in range(4):
        ni = pos[0] + di[k]
        nj = pos[1] + dj[k]
        if 0 <= ni < N and 0 <= nj < M and d != ((k + 2) % 4):
            put_block(matrix, (ni, nj), k, res, step + 1)


def put_fuck(matrix, pos):
    global max_v
    block_sum = [matrix[pos[0]][pos[1]]]

    for k in range(4):
        ni = pos[0] + di[k]
        nj = pos[1] + dj[k]
        if 0 <= ni < N and 0 <= nj < M:
            block_sum.append(matrix[ni][nj])

    if len(block_sum) == 3:
        return
    elif len(block_sum) == 4:
        max_v = max(max_v, sum(block_sum))
        return
    else:
        sum_v = sum(block_sum)
        for k in range(1, 5):
            max_v = max(max_v, (sum_v - block_sum[k]))
        return


if __name__ == "__main__":
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_point = max(map(max, matrix))

    max_v = 0
    for i in range(N):
        for j in range(M):
            put_block(matrix, (i, j))
            put_fuck(matrix, (i, j))

    print(max_v)
