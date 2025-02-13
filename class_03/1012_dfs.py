import sys

input = sys.stdin.readline

T = int(input())

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def dfs(i, j):
    if matrix[i][j] == 0:
        return False
    
    stack = [(i, j)]
    matrix[i][j] = 0

    while stack:
        ci, cj = stack.pop()
        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]
            if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj] != 0:
                matrix[ni][nj] = 0
                stack.append((ni, nj))
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
            if dfs(r, c):
                min_worm += 1

    print(min_worm)
