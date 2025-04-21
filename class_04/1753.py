from heapq import heappop, heappush
import sys

input = lambda:sys.stdin.readline()
out = lambda x:sys.stdout.write(x + "\n")

def dijkstra(s):
    heap = [(0, s)]
    visited = [False] * (V + 1)
    dist = [float("inf")] * (V + 1)
    dist[s] = 0

    while heap:
        d, v = heappop(heap)
        if visited[v]:
            continue
        visited[v] = True

        for tv, td in graph[v]:
            nd = d + td
            if dist[tv] > nd:
                dist[tv] = nd
                heappush(heap, (nd, tv))
    return visited, dist


V, E = map(int, input().split())
S = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

visited, dist = dijkstra(S)
for i in range(1, (V + 1)):
    if visited[i]:
        out(str(dist[i]))
    else:
        out("INF")