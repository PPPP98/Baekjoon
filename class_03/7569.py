import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()
out = lambda x: sys.stdout.write(x)

d = ((-1, 0, 0), (0, 1, 0), (1, 0, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def bfs():
    que = deque()
    # find start
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if matrix[h][r][c] == 1:
                    que.append((r, c, h))
    while que:
        i, j, k = que.popleft()
        for di, dj, dk in d:
            ni, nj, nk = i + di, j + dj, k + dk
            if 0 <= ni < N and 0 <= nj < M and 0 <= nk < H and matrix[nk][ni][nj] == 0:
                matrix[nk][ni][nj] = matrix[k][i][j] + 1
                que.append((ni, nj, nk))
    return


def check():
    res = 0
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if matrix[h][r][c] == 0:
                    return -1
                res = max(res, matrix[h][r][c])

    return res - 1


if __name__ == "__main__":
    M, N, H = map(int, input().split())
    matrix = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
    bfs()
    out(str(check()))
