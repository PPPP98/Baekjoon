import sys

input = sys.stdin.readline
print = sys.stdout.write


def fibonacci(n: int):
    cache = [[1, 0], [0, 1], [1, 1]]
    for i in range(3, n + 1):
        cnt = [cache[i - 1][0] + cache[i - 2][0], cache[i - 1][1] + cache[i - 2][1]]
        cache.append(cnt)
    return cache[n]


T = int(input())

for _ in range(T):
    N = int(input())
    N_cnt = fibonacci(N)
    print(f"{N_cnt[0]} {N_cnt[1]}\n")
