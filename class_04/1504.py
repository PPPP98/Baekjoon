from heapq import heappop, heappush
import sys

input = lambda:sys.stdin.readline()

def dijkstra(s, e):
    heap = [(0, s)]
    visited = [False] * (N + 1)
    dist = [float("inf")] * (N + 1)
    dist[s] = 0

    while heap:
        d, v = heappop(heap)
        if visited[v]:
            continue
        if v == e:
            return d
        visited[v] = True

        for n_v, w in graph[v]:
            n_d = w + d
            if dist[n_v] > n_d:
                dist[n_v] = n_d
                heappush(heap, (n_d, n_v))
    if not visited[e]:
        return -1


N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int ,input().split())

start1 = dijkstra(1, v1)
start2 = dijkstra(1, v2)
end1 = dijkstra(v2, N)
end2 = dijkstra(v1, N)
mid = dijkstra(v1, v2)

ans = float("inf")
if mid != -1:
    ans1, ans2 = float("inf"), float("inf")
    if ((start1 != -1) and (end1 != -1)):
        ans1 = start1 + end1 + mid
    if ((start2 != -1) and (end2 != -1)):
        ans2 = start2 + end2 + mid
    ans = min(ans1, ans2)

if ans != float("inf"):
    print(ans)
else:
    print(-1)
