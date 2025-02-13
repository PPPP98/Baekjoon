import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def bfs(i, j):
    if matrix[i][j] == 0:
        return False
    
    que = deque()
    que.append((i, j))
    matrix[i][j] = 0

    while que:
        ci, cj = que.popleft()
        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj] != 0:
                matrix[ni][nj] = 0
                que.append((ni, nj))
    return True


for _ in range(T):
    M, N, K = map(int, input().split())
    matrix = [[0] * M for i in range(N)]
    min_worm = 0

    for x in range(K):
        j, i = map(int, input().split())
        matrix[i][j] = 1

    for r in range(N):
        for c in range(M):
            if bfs(r, c):
                min_worm += 1

    print(min_worm)
