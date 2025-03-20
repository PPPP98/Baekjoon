class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        tx, ty = self.find(x), self.find(y)
        if tx == ty:
            return False

        if self.rank[tx] > self.rank[ty]:
            self.parent[ty] = tx
        elif self.rank[ty] > self.rank[tx]:
            self.parent[tx] = ty
        else:
            self.parent[ty] = tx
            self.rank[tx] += 1

        return True


def kruskal(n, edges: list):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    check = 0
    res = 0
    for s, e, w in edges:
        if uf.union(s, e):
            res += w
            check += 1
            if check == (n - 1):
                return res


def solve():
    T = int(input())
    for tc in range(1, T + 1):
        V, E = map(int, input().split())
        edges = [tuple(map(int, input().split())) for _ in range(E)]
        ans = kruskal(V, edges)
        print(f"#{tc} {ans}")


if __name__ == "__main__":
    solve()
