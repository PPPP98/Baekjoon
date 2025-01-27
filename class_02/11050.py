import sys

input = sys.stdin.readline()


def binomial(n, k):
    if n == k or k == 0:
        return 1
    # 캐쉬 공간 생성 - 중복 계산 방지 / 점화식
    cache = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    # k = 0 일 때 값은 1
    for i in range(n + 1):
        cache[i][0] = 1
    # n = k 일 때 값은 1
    for i in range(k + 1):
        cache[i][i] = 1

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            cache[i][j] = cache[i - 1][j] + cache[i - 1][j - 1]
    
    return cache[i][j]

N, K = map(int, input.split())
print(binomial(N, K))