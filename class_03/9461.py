T = int(input())


for _ in range(T):
    N = int(input())
    cache = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

    if len(cache) <= N:
        for i in range(11, N + 1):
            cache.append(cache[i - 1] + cache[i - 5])

    print(cache[N])
