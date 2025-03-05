import sys
import heapq
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())

heap = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if heap:
            print(str(heapq.heappop(heap)) + "\n")
        else:
            print("0\n")
    else:
        heapq.heappush(heap, x)

