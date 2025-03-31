import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()
out = lambda x: sys.stdout.write(str(x) + "\n")


def bfs():
    que = deque([1])
    visited = [0] * (N + 1)
    visited[1] = 1
    while que:
        v = que.popleft()
        for w in tree[v]:
            if not visited[w]:
                visited[w] = v
                que.append(w)
    return visited


N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

res = bfs()
for i in range(2, N + 1):
    out(res[i])
