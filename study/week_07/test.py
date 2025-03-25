d = ((0, 1), (1, 0), (0, -1), (-1, 0))
 
 
def backtracking(matrix, done, connect, length=0):
    global max_cnt, min_len

 
    if done == M:
        if connect == max_cnt:
            min_len = length if min_len > length else min_len
        elif connect > max_cnt:
            max_cnt = connect
            min_len = length
        return
 
    for i, j in core:
        if matrix[i][j] == 3:
            continue
 
        for di, dj in d:
            x = 1
 
            stack = []
            while True:
                ni, nj = i + (di * x), j + (dj * x)
                if (ni < 0 or nj < 0) or (ni == N or nj == N):
                    for r, c in stack:
                        matrix[r][c] = 2
                        length += 1
                    matrix[i][j] = 3
                    backtracking(matrix, done + 1, connect + 1, length)
                    for r, c in stack:
                        matrix[r][c] = 0
                        length -= 1
                    matrix[i][j] = 1
                    break
 
                if matrix[ni][nj] != 0:
                    matrix[i][j] = 3
                    backtracking(matrix, done + 1, connect, length)
                    matrix[i][j] = 1
                    break
                else:
                    x += 1
                    stack.append((ni, nj))
        else:
            break
 
 
T = int(input())
 
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
 
    M = 0
    done = 0
    core = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                M += 1
                core.append((i, j))
                if i == 0 or j == 0 or i == (N - 1) or j == (N - 1):
                    done += 1
                    matrix[i][j] = 3
                    core.pop()
 
    max_cnt = 0
    min_len = float("inf")
 
    backtracking(matrix, done, done)
    print(f"#{tc} {min_len}")