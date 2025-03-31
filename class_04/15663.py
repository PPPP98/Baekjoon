import sys

input = lambda: sys.stdin.readline().strip()


def back(cnt):
    if cnt == M:
        now = tuple(res)
        if now not in visited:
            print(*res)
        visited.add(now)
        return

    for i in range(N):
        if not select[i]:
            select[i] = True
            res.append(arr[i])
            back(cnt + 1)
            res.pop()
            select[i] = False


N, M = map(int, input().split())

arr = sorted(map(int, input().split()))

res = []
select = [False] * N
visited = set()
back(0)
