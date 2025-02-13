def fibo(num):
    cache = [0, 1, 1]
    for i in range(3, num + 1):
        cache.append(cache[i - 1] + cache[i - 2])
    
    return cache[num]

N = int(input())

print(fibo(N))