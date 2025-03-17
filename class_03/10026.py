import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()


def bfs(start, color: set, visited: list, matrix: list):
    que = deque([start])
    N = len(matrix)
    while que:
        i, j = que.popleft()
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and matrix[ni][nj] in color:
                visited[ni][nj] = True
                que.append((ni, nj))
    return


def solve():
    N = int(input())
    matrix = [list(input()) for _ in range(N)]
    cnt_1 = cnt_2 = 0

    visited = [[False] * N for _ in range(N)]
    visited_2 = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs((i, j), {matrix[i][j]}, visited, matrix)
                cnt_1 += 1
            if not visited_2[i][j]:
                if matrix[i][j] == "G" or matrix[i][j] == "R":
                    bfs((i, j), {"R", "G"}, visited_2, matrix)
                else:
                    bfs((i, j), {"B"}, visited_2, matrix)
                cnt_2 += 1

    print(cnt_1, cnt_2)

if __name__ == "__main__":
    solve()