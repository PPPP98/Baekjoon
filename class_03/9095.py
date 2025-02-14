import sys
input = sys.stdin.readline

T = int(input())


for _ in range(T):
    N = int(input())
    cache = [0, 1, 2, 4]

    for i in range(4, N + 1):
        cache.append(cache[i - 1] + cache[i - 2] + cache[i - 3])
    
    print(cache[N])