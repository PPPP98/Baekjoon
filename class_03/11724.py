import sys
from collections import deque

input = sys.stdin.readline


def bfs(s):
    que = deque([s])
    visited[s] = True
    while que:
        v = que.popleft()
        for w in graph[v]:
            if not visited[w]:
                visited[w] = True
                que.append(w)


N, M = map(int, input().split())

graph = [[] for _ in range(1 + N)]

for _ in range(M):
    v, e = map(int, input().split())
    graph[v].append(e)
    graph[e].append(v)

visited = [False] * (N + 1)

result = 0
for i in range(1, N + 1):
    if not visited[i]:
        bfs(i)
        result += 1

print(result)