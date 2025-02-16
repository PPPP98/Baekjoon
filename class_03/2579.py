# f(n) = max(f(n - 2), step[n - 1] + f(n - 3))

import sys
input = sys.stdin.readline

def max_score(n):
    cache1 = [0] * (n + 1)
    cache2 = [0] * (n + 1)
    if n == 1:
        return step[0]

    cache1[1] = step[0]
    cache1[2] = step[1] + step[0]

    cache2[2] = step[1]

    for i in range(3, n + 1):
        cache1[i] = step[i - 1] + max(cache1[i - 2], step[i - 2] + cache1[i - 3])
        cache2[i] = step[i - 1] + max(cache2[i - 2], step[i - 2] + cache2[i - 3])
    return max(cache1[n], cache2[n])


N = int(input())

step = [int(input()) for _ in range(N)]

print(max_score(N))
