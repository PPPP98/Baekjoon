import sys
import heapq

input = lambda: sys.stdin.readline().strip()


def dijkstra():
    heap = [(0, A)]
    dist = [float("inf")] * (N + 1)
    visited = [False] * (N + 1)
    dist[A] = 0

    while heap:
        d, v = heapq.heappop(heap)
        if visited[v]:
            continue
        if v == B:
            return d
        visited[v] = True
        for w, e in edges[v]:
            next_d = d + w
            if dist[e] > next_d:
                dist[e] = next_d
                heapq.heappush(heap, (next_d, e))


N = int(input())
M = int(input())
edges = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e, w = map(int, input().split())
    edges[s].append((w, e))

A, B = map(int, input().split())

ans = dijkstra()
print(ans)