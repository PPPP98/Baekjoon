import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]


def bfs(start, matrix):
    que = deque([start])
    visited = [[False] * M for _ in range(N)]
    visited[start[0]][start[1]] = True
    matrix[start[0]][start[1]] = 0
    while que:
        i, j = que.popleft()
        for di, dj in ((1,0),(0,1),(-1,0),(0,-1)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj] and matrix[ni][nj] == 1:
                visited[ni][nj] = True
                matrix[ni][nj] = matrix[i][j] + 1
                que.append((ni, nj))

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and matrix[i][j] == 1:
                matrix[i][j] = -1



start = False
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 2:
            start = (i, j)
            break
    if start:
        break



bfs(start, matrix)

for i in range(N):
    print(* matrix[i])
