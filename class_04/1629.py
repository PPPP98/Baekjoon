def back(idx):
    if idx == 1:
        return A % C

    if idx % 2 == 1:
        t = back(idx // 2)
        return (t * t * A) % C
    else:
        t = back(idx // 2)
        return (t * t) % C


A, B, C = map(int, input().split())
res = back(B)
print(res)
