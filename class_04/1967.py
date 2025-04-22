import sys

input = lambda: sys.stdin.readline()


def dfs(x):
    q = [(x, 0)]
    visited = [False] * (N + 1)
    visited[x] = True
    max_d = 0

    while q:
        v, d = q.pop()
        if d > max_d:
            max_d = d
        for n, w in graph[v]:
            if not visited[n]:
                visited[n] = True
                q.append((n, d + w))
    return max_d


N = int(input())

graph = [[] for _ in range(N + 1)]
child = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    p, c, d = map(int, input().split())
    child[p].append((c, d))
    graph[p].append((c, d))
    graph[c].append((p, d))

leaf = [x for x in range(1, N + 1) if not child[x]]

ans = [0] * len(leaf)
for i in range(len(leaf)):
    ans[i] = dfs(leaf[i])

print(max(ans))
