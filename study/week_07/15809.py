import sys

input = lambda: sys.stdin.readline().strip()
out = lambda x: sys.stdout.write(x + "\n")


def find(x):
    if alliance[x] == x:
        return x
    alliance[x] = find(alliance[x])
    return alliance[x]


def play(cmd, x, y):
    if cmd == 1:
        alliance[y] = x
        rank[x] += rank[y]
        rank[y] = 0
    elif cmd == 2:
        alliance[y] = x
        rank[x] -= rank[y]
        rank[y] = 0


def union(cmd, x, y):
    p_x = find(x)
    p_y = find(y)

    if rank[p_x] > rank[p_y]:
        play(cmd, p_x, p_y)
    elif rank[p_x] < rank[p_y]:
        play(cmd, p_y, p_x)
    else:
        play(cmd, p_x, p_y)


if __name__ == "__main__":
    N, M = map(int, input().split())
    alliance = [i for i in range(N + 1)]
    rank = [0] * (N + 1)
    for i in range(1, N + 1):
        rank[i] = int(input())

    for x in range(M):
        O, P, Q = map(int, input().split())
        union(O, P, Q)

    res = [x for x in rank if x != 0]
    res.sort()

    out(str(len(res)))
    out(" ".join(map(str, res)))
