from collections import deque

def bfs(s):
    visited = [False] * (100000 + 1)
    que = deque([(s, 0)])
    visited[s] = True
    if s == K:
        return 0
    while que:
        v, step = que.popleft()
        if v < K:
            for w in [v * 2, v + 1, v - 1]:
                if 0 <= w <= 100000 and not visited[w]:
                    if w == K:
                        return step + 1
                    visited[w] = True
                    next = step + 1
                    que.append((w, next))
        else:
            w = v - 1
            if 0 <= w <= 100000 and not visited[w]:
                if w == K:
                    return step + 1
                visited[w] = True
                next = step + 1
                que.append((w, next))


N, K = map(int, input().split())


print(bfs(N))



