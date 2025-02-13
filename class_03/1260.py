import sys
from collections import deque

input = sys.stdin.readline

def dfs_search(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    if v in graph:
        for i in graph[v]:
            if not visited[i]:
                dfs_search(graph, i, visited)

def bfs_search(graph, v, visited):
    que = deque([v])
    visited[v] = True

    while que:
        v = que.popleft() # 큐에 있는 첫번째 노드를 꺼낸 후
        print(v, end=' ') # 출력
        if v in graph:
            for i in graph[v]:
                if not visited[i]:
                    que.append(i)
                    visited[i] = True


N, M, V = map(int, input().split())


graph = {}

for i in range(M):
    n1, n2 = map(int, input().split())
    if n1 not in graph:
        graph[n1] = set()
    if n2 not in graph:
        graph[n2] = set()

    graph[n1].add(n2)
    graph[n2].add(n1)

for node in graph:
    graph[node] = sorted(graph[node])

visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

dfs_search(graph, V, visited_dfs)
print()
bfs_search(graph, V, visited_bfs)