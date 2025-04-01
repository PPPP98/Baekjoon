import sys

input = lambda: sys.stdin.readline().strip()


def back(idx, cnt):
    if idx == L:
        return
    if cnt == M:
        print(*select)
        return

    for i in range(idx, L):
        select.append(arr[i])
        back(i, cnt + 1)
        select.pop()


N, M = map(int, input().split())
arr = sorted(set(map(int, input().split())))
L = len(arr)
select = []
back(0, 0)
