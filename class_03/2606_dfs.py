import sys
input = sys.stdin.readline
visit = 0

def dfs(graph, v, visited):
    visited[v] = True
    global visit
    visit += 1
    if v in graph:
        for i in graph[v]:
            if not visited[i]:
                dfs(graph, i, visited)


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

dfs(graph, 1, visited)

print(visit - 1)
