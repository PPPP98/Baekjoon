import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    priority = list(map(int, input().split()))
    line = list(range(N))
    target = M

    count = 1
    while True:
        if priority[0] < max(priority):
            priority.append(priority.pop(0))
            if target == 0:
                target += len(priority)
            target -= 1
        else:
            if target == 0:
                print(count)
                break
            priority.pop(0)
            count += 1
            target -= 1
