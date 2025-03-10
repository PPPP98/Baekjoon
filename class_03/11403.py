import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()


def init(N: int) -> list:
    return [list(map(int, input().split())) for _ in range(N)]


def bfs(graph: list, size: int, start: int) -> list:
    visited = [0] * size
    q = deque([start])
    while q:
        v = q.popleft()
        for w in range(size):
            if graph[v][w] and not visited[w]:
                visited[w] = 1
                q.append(w)
    return visited


def main():
    N = int(input())
    graph = init(N)
    result = []
    for i in range(N):
        result.append(bfs(graph, N, i))

    for i in range(N):
        print(*result[i])


main()
