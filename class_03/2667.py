import sys
from collections import deque

input = sys.stdin.readline


def bfs(matrix, n, pos):
    que = deque([pos])
    cnt = 1
    matrix[pos[0]][pos[1]] = 0
    while que:
        i, j = que.popleft()
        for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < n and matrix[ni][nj] == 1:
                matrix[ni][nj] = 0
                que.append((ni, nj))
                cnt += 1
    
    return cnt


if __name__ == "__main__":
    N = int(input())
    matrix = [list(map(int, input().strip())) for _ in range(N)]

    house_cnt = []
    cnt = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                house_cnt.append(bfs(matrix, N, (i, j)))
                cnt += 1
    
    house_cnt.sort()
    print(cnt)
    print('\n'.join(map(str, house_cnt)))
