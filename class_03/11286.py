import heapq
import sys
input = sys.stdin.readline

N = int(input())

heap = []
result = []
for _ in range(N):
    num = int(input())
    if num < 0:
        heapq.heappush(heap, (-num, -1))
    elif num > 0:
        heapq.heappush(heap, (num, 1))
    else:
        if heap:
            temp = heapq.heappop(heap)
            result.append(str(temp[0] * temp[1]))
        else:
            result.append("0")

print("\n".join(result))