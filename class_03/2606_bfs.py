import sys
from collections import deque

input = sys.stdin.readline


visit = 0


def bfs(graph, v, visited):
    que = deque([v])
    visited[v] = True
    global visit
    while que:
        v = que.popleft()
        if v in graph:
            for i in graph[v]:
                if not visited[i]:
                    que.append(i)
                    visited[i] = True
                    visit += 1




computer = int(input())
connect = int(input())

graph = {}
for i in range(connect):
    n, v = map(int, input().split())

    if n not in graph:
        graph[n] = set()
    if v not in graph:
        graph[v] = set()

    graph[n].add(v)
    graph[v].add(n)

visited = [False] * (computer + 1)

bfs(graph, 1, visited)

print(visit)
