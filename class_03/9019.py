import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()
out = lambda x: sys.stdout.write(x + "\n")


def cal(num, cmd):
    if cmd == "D":
        return (num * 2) % 10000
    elif cmd == "S":
        return num - 1 if num > 0 else 9999
    elif cmd == "L":
        temp = num * 10
        a, b = divmod(temp, 10000)
        return b + a
    elif cmd == "R":
        a, b = divmod(num, 10)
        return (b * 1000) + a


def bfs():
    que = deque()
    visited = [0] * 10000
    visited[A] = True
    que.append((A, ""))

    while que:
        now, step = que.popleft()
        if now == B:
            return step
        for x in ("D", "S", "L", "R"):
            temp = cal(now, x)
            if not visited[temp]:
                visited[temp] = 1
                next_step = step + x
                que.append((temp, next_step))
    return


if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T + 1):
        A, B = map(int, input().split())
        ans = bfs()
        out(ans)
