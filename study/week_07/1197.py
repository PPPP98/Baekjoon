from heapq import heappop, heappush


def prim(n: int, edges: list) -> int:
    visited = [False] * (n + 1)
    heap = [(0, 1)]
    check = 0
    res = 0
    while heap:
        w, v = heappop(heap)
        if not visited[v]:
            visited[v] = True
            check += 1
            res += w
            if check == n:
                return res
            for weight, node in edges[v]:
                if not visited[node]:
                    heappush(heap, (weight, node))


if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T + 1):
        V, E = map(int, input().split())
        edges = [[] for _ in range(V + 1)]
        for _ in range(E):
            s, e, w = map(int, input().split())
            edges[s].append((w, e))
            edges[e].append((w, s))

        ans = prim(V, edges)
        print(f"#{tc} {ans}")
