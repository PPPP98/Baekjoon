from collections import deque


def cal(num, cmd):
    if cmd == 1:
        return num * 2
    else:
        return num * 10 + 1


def bfs():
    que = deque([(A, 1)])
    while que:
        now, step = que.popleft()
        for x in [0, 1]:
            next_num = cal(now, x)
            if next_num == B:
                return step + 1
            elif next_num > B:
                continue
            else:
                que.append((next_num, step + 1))
    return -1


if __name__ == "__main__":
    A, B = map(int, input().split())
    ans = bfs()
    print(ans)
