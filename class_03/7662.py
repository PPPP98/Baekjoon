import sys
from heapq import heappop, heappush

input = lambda:sys.stdin.readline().strip()

T = int(input())

for tc in range(T):
    N = int(input())
    data = {}
    min_heap = []
    max_heap = []
    cnt = 0
    for _ in range(N):
        cal, x = input().split()
        x = int(x)
        if cal == "I":
            if x not in data:
                data[x] = 0
            data[x] += 1
            cnt += 1
            heappush(min_heap, x)
            heappush(max_heap, -x)
        elif cal == "D":
            if cnt > 0:
                if x == 1:
                    while not data[-max_heap[0]]:
                        heappop(max_heap)
                    data[-heappop(max_heap)] -= 1
                elif x == -1:
                    while not data[min_heap[0]]:
                        heappop(min_heap)
                    data[heappop(min_heap)] -= 1
                cnt -= 1


    if cnt == 0:
        print("EMPTY")
    else:
        while not data[-max_heap[0]]:
            heappop(max_heap)
        while not data[min_heap[0]]:
            heappop(min_heap)

        print(-heappop(max_heap), heappop(min_heap))