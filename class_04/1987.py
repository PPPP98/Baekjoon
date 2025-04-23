import sys

input = lambda:sys.stdin.readline()

d = ((0, 1), (1, 0), (0, -1), (-1, 0))


def dfs(i, j, mask, cnt):
    global max_v
    if max_v == 26:
        return
    max_v = max(max_v, cnt)
    for di, dj in d:
        ni, nj = i + di, j + dj
        if 0 <= ni < R and 0 <= nj < C:
            now = 1 << (ord(board[ni][nj]) - ord("A"))
            if not (mask & now):
                dfs(ni, nj, mask | now, cnt + 1)


R, C = map(int, input().split())
board = [input().strip() for _ in range(R)]

max_v = 0
visited = 1 << (ord(board[0][0]) - ord("A"))

dfs(0, 0, visited, 1)
print(max_v)
