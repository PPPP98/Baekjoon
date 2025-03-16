import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()


def bfs(matrix: list):
    que = deque()
    max_v = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                que.append((i, j))
    while que:
        i, j = que.popleft()
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj] == 0:
                matrix[ni][nj] = matrix[i][j] + 1
                que.append((ni, nj))

    for i in range(N):
        if not all(matrix[i]):
            return -1
        max_v = max(max_v, max(matrix[i]))
    else:
        return max_v - 1


if __name__ == "__main__":
    M, N = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    ans = bfs(matrix)
    print(ans)
