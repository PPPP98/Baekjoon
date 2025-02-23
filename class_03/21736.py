import sys
from collections import deque

input = sys.stdin.readline


# O는 빈 공간, X는 벽, I는 도연이, P는 사람
def bfs(s):
    visited = [[False] * M for _ in range(N)]
    que = deque([s])
    visited[s[0]][s[1]] = True
    cnt = 0
    while que:
        i, j = que.popleft()
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni = i + di
            nj = j + dj
            if (
                0 <= ni < N
                and 0 <= nj < M
                and not visited[ni][nj]
                and campus[ni][nj] != "X"
            ):
                visited[ni][nj] = True
                que.append((ni, nj))
                if campus[ni][nj] == "P":
                    cnt += 1

    if cnt:
        return cnt
    else:
        return "TT"


if __name__ == "__main__":
    N, M = map(int, input().split())
    campus = [list(input().strip()) for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if campus[i][j] == "I":
                start = (i, j)
                break

    print(f"{bfs(start)}")
