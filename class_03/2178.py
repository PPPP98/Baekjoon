from collections import deque
import sys

input = sys.stdin.readline


def bfs(s, e):
    que = deque([s])
    visited = [[0] * M for _ in range(N)]
    visited[s[0]][s[1]] = 1

    while que:
        i, j = que.popleft()
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and maze[ni][nj] == 1 and not visited[ni][nj]:
                if ni == e[0] and nj == e[1]:
                    return visited[i][j] + 1
                else:
                    visited[ni][nj] += visited[i][j] + 1
                    que.append((ni, nj))




N, M = map(int, input().split())

maze = [list(map(int, input().strip())) for _ in range(N)]

print(bfs((0, 0), (N - 1, M - 1)))