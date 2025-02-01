# 1 2 3 4 5 6 7
import sys
from collections import deque

print = sys.stdout.write

N, K = map(int, sys.stdin.readline().split())

Que = deque(range(1, N + 1))
new_arr = []

while len(Que) > 1:
    for _ in range(K - 1):
        Que.append(Que.popleft())
    new_arr.append(Que.popleft())

new_arr.append(Que.popleft())

print(f"<{', '.join(map(str, new_arr))}>")
