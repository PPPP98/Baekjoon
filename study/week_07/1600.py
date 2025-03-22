import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

move = ((0, 1), (1, 0), (-1, 0), (0, -1))
jump = ((1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2))
INF = 200 * 200


def bfs(skill: int, width: int, height: int, matrix: list) -> int:
    visited = [[-1] * width for _ in range(height)]
    visited[0][0] = skill
    # i, j, jump, move
    que = deque([(0, 0, skill, 0)])
    while que:
        i, j, k, m = que.popleft()
        if i == height - 1 and j == width - 1:
            return m

        for di, dj in move:
            ni, nj = i + di, j + dj
            if 0 <= ni < height and 0 <= nj < width and matrix[ni][nj] != 1:
                if visited[ni][nj] < k:
                    visited[ni][nj] = k
                    que.append((ni, nj, k, m + 1))

        if k > 0:
            for di, dj in jump:
                ni, nj = i + di, j + dj
                if 0 <= ni < height and 0 <= nj < width and matrix[ni][nj] != 1:
                    if visited[ni][nj] < k - 1:
                        visited[ni][nj] = k - 1
                        que.append((ni, nj, k - 1, m + 1))

    return -1


def solve():
    K = int(input())
    W, H = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(H)]

    ans = bfs(K, W, H, matrix)
    print(ans)


if __name__ == "__main__":
    solve()
