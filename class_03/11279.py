import heapq
import sys
input = sys.stdin.readline

heap = []

N = int(input())

for _ in range(N):
    cmd = int(input())
    if cmd:
        heapq.heappush(heap, -cmd)
    else:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)