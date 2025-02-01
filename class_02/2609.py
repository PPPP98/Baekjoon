A, B = map(int, input().split())


def gcd(b, r):
    if b % r == 0:
        return r
    else:
        return gcd(r, b % r)


if A < B:
    N = gcd(B, A)
else:
    N = gcd(A, B)

print(N, (A * B) // (N))
