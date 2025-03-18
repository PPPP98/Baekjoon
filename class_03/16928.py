import sys
from collections import deque

# 1 ~ 6 dice / 1 to 100
input = lambda: sys.stdin.readline().strip()


def bfs():
    que = deque([1])
    visited = [0] * 101
    visited[1] = 1
    while que:
        idx = que.popleft()
        for i in range(1, 7):
            next_idx = idx + i
            if next_idx == 100:
                return visited[idx]
            if next_idx <= 100 and not visited[next_idx]:
                visited[next_idx] = visited[idx] + 1
                if next_idx in ladder:
                    temp = ladder[next_idx]
                    if not visited[temp]:
                        visited[temp] = visited[idx] + 1
                        que.append(temp)

                elif next_idx in snake:
                    temp = snake[next_idx]
                    if not visited[temp]:
                        visited[temp] = visited[idx] + 1
                        que.append(temp)
                else:
                    que.append(next_idx)


if __name__ == "__main__":
    N, M = map(int, input().split())
    ladder = {}
    snake = {}
    for _ in range(N):
        s, e = map(int, input().split())
        ladder[s] = e
    for _ in range(M):
        s, e = map(int, input().split())
        snake[s] = e

    ans = bfs()
    print(ans)
