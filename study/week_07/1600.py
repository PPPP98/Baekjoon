import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

move = (
    (0, 1, 0),
    (1, 0, 0),
    (-1, 0, 0),
    (0, -1, 0),
    (1, 2, 1),
    (2, 1, 1),
    (2, -1, 1),
    (1, -2, 1),
    (-1, -2, 1),
    (-2, -1, 1),
    (-2, 1, 1),
    (-1, 2, 1),
)
INF = 200 * 200


def bfs(skill: int, width: int, height: int, matrix: list) -> int:
    distance = [[[INF] * width for _ in range(height)] for _ in range(skill + 1)]
    for x in range(skill + 1):
        distance[x][0][0] = 1

    que = deque([(0, 0, 0)])

    if (0, 0) == (width - 1, height - 1):
        return 0

    while que:
        i, j, k = que.popleft()
        for di, dj, dk in move:
            ni, nj, nk = i + di, j + dj, k + dk
            if (
                0 <= ni < height
                and 0 <= nj < width
                and nk <= skill
                and distance[nk][ni][nj] == INF
                and matrix[ni][nj] != 1
            ):
                if (ni, nj) == (height - 1, width - 1):
                    return distance[k][i][j]
                distance[nk][ni][nj] = distance[k][i][j] + 1

                for x in range(nk, skill + 1):
                    if distance[x][ni][nj] > distance[nk][ni][nj]:
                        distance[x][ni][nj] = distance[nk][ni][nj]

                que.append((ni, nj, nk))

    return -1


def solve():
    K = int(input())
    W, H = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(H)]

    ans = bfs(K, W, H, matrix)
    print(ans)


if __name__ == "__main__":
    solve()
