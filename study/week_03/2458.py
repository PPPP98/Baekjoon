import sys
input = sys.stdin.readline

def dfs(v, field):
    visited = [False] * (N + 1)
    visited[v] = True
    cnt = 0
    stack = []

    stack.append(v)
    while stack:
        v = stack.pop()
        for w in field[v]:
            if not visited[w]:
                visited[w] = True
                cnt += 1
                stack.append(w)
    return cnt


N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
parent = [[] for _ in range(N + 1)]

for _ in range(M):
    v, e = map(int, input().split())
    graph[v].append(e)
    parent[e].append(v)

result = 0
for i in range(1, N + 1):
    member = dfs(i, graph) + dfs(i, parent)
    if member == (N - 1):
        result += 1

print(result)