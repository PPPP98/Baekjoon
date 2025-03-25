import sys

input = lambda: sys.stdin.readline().strip()


def bellman_ford(N: int, edges: list):
    INF = float("inf")
    dist = [INF] * (N + 1)
    dist[1] = 0

    for _ in range(N - 1):
        for s, e, t in edges:
            if dist[s] != INF and dist[e] > dist[s] + t:
                dist[e] = dist[s] + t

    for s, e, t in edges:
        if dist[s] != INF and dist[e] > dist[s] + t:
            return -1

    res = [dist[i] if dist[i] != INF else -1 for i in range(2, N + 1)]
    return "\n".join(map(str, res))


def solve():
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        edges.append(tuple(map(int, input().split())))

    ans = bellman_ford(N, edges)
    print(ans)


if __name__ == "__main__":
    solve()
