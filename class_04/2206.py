from collections import deque
import sys

input = lambda: sys.stdin.readline().strip()


def bfs():
    if N == 1 and M == 1:
        return 1
    
    visited = [[0] * M for _ in range(N)]
    q = deque([(0, 0, 1, 2)])
    visited[0][0] = 2

    while q:
        i, j, d, b = q.popleft()
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and (visited[ni][nj] < b):
                if b == 1 and matrix[ni][nj] == 1:
                    continue
                elif b == 2 and matrix[ni][nj] == 1:
                    nb = 1
                else:
                    nb = b
                if ni == N - 1 and nj == M - 1:
                    return d + 1
                visited[ni][nj] = nb
                q.append((ni, nj, d + 1, nb))

    return -1


N, M = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(N)]

print(bfs())