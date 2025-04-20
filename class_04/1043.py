def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y, u=True):
    px = find(x)
    py = find(y)
    if px == py:
        return False
    if u:
        parent[py] = px
    return True

N, M = map(int, input().split())
parent = [i for i in range(N + 1)]

arr = list(map(int, input().split()))
for i in range(1, arr[0]  + 1):
    union(0, arr[i])

data = []

for i in range(M):
    data.append(list(map(int, input().split())))
    if data[i][0] > 1:
        for j in range(2, data[i][0] + 1):
            union(data[i][1], data[i][j])

res = 0
for i in range(M):
    if union(0, data[i][1], False):
        res += 1

print(res)
