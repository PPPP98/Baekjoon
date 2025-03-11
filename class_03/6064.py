import sys
import math

input = lambda: sys.stdin.readline().strip()
print = lambda x:sys.stdout.write(x)

def init():
    M, N, x, y = map(int, input().split())
    if M > N:
        return (M, N, x, y)
    else:
        return (N, M, y, x)


def kain(M: int, N: int, x_target: int, y_target: int) -> int:
    year = 1
    x = y = 1
    cycle = 0
    LCM = (M * N) // math.gcd(M, N)

    step = M
    target = x_target

    while year <= LCM:
        if x == x_target and y == y_target:
            return year
        now = cycle * step + target

        x = target
        y = now % N if now % N != 0 else N

        year = now
        cycle += 1
    return -1


def main():
    T = int(input())
    result = [0] * T
    for tc in range(T):
        result[tc] = str(kain(*init()))
    print("\n".join(result))


main()
