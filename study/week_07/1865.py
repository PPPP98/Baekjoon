import sys

input = lambda: sys.stdin.readline().strip()


def bellman_ford(N: int, graph: list):
    INF = (N) * 10000
    dist = [INF] * (N + 1)
    dist[1] = 0

    for _ in range(N - 1):
        for s, e, w in graph:
            if dist[s] + w < dist[e]:
                dist[e] = dist[s] + w

    for s, e, w in graph:
        if dist[s] + w < dist[e]:
            return "YES"

    return "NO"


def solve():
    T = int(input())

    for tc in range(T):
        N, M, W = map(int, input().split())

        graph = []
        for _ in range(M):
            s, e, w = map(int, input().split())
            graph.append((s, e, w))
            graph.append((e, s, w))

        for _ in range(W):
            s, e, w = map(int, input().split())
            graph.append((s, e, -w))

        ans = bellman_ford(N, graph)
        print(ans)


if __name__ == "__main__":
    solve()