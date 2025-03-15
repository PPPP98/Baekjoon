import sys
from heapq import heappush, heappop

input = lambda:sys.stdin.readline().strip()
out = lambda x:sys.stdout.write(x + "\n")

def solve():
    N = int(input())
    schedule = []
    for _ in range(N):
        s, e = map(int, input().split())
        heappush(schedule, (e, s))

    pivot = 0
    cnt = 0
    for i in range(N):
        temp = heappop(schedule)
        if pivot <= temp[1]:
            pivot = temp[0]
            cnt += 1
    out(str(cnt))

solve()