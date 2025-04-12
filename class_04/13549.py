from heapq import heappop, heappush

INF = float("inf")

def find():
    dist = [INF] * 100001
    dist[N] = 0
    visited = [False] * 100001
    heap = [(0, N)]

    while heap:
        t, x = heappop(heap)
        if visited[x]:
            continue
        if x == K:
            return t
        visited[x] = True
        for i in (-1, 0, 1):
            if i: 
                nx = x + i
                if 0 <= nx <= 100000 and dist[nx] > t + 1:
                    dist[nx] = t + 1
                    heappush(heap, (t + 1, nx))
            else:
                nx = x * 2
                if 0 <= nx <= 100000 and dist[nx] > t:
                    dist[nx] = t
                    heappush(heap, (t, nx))


N, K = map(int, input().split())

ans = find()
print(ans)