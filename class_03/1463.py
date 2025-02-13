def made_one(num):
    cache = [0, 0, 1, 1]

    for i in range(4, num + 1):
        n1 = n2 = n3 = float("inf")
        if i % 2 == 0:
            n1 = cache[i // 2] + 1
        if i % 3 == 0:
            n2 = cache[i // 3] + 1
        n3 = cache[i - 1] + 1

        cache.append(min(n1, n2, n3))
    
    return cache[num]


N = int(input())

print(f"{made_one(N)}")