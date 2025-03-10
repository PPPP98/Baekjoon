# 이진트리가 아닌 일반트리 -> 전위 후위 중위 순회 불가

import sys

input = lambda: sys.stdin.readline().strip()
print = lambda x:sys.stdout.write(x)

def insert(N):
    tree = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        n1, n2 = map(int, input().split())
        tree[n1].append(n2)
        tree[n2].append(n1)
    return tree


def LCA(n1: int, n2: int, depth: list, parent: list) -> str:
    # find parent
    depth_1 = depth[n1]
    depth_2 = depth[n2]

    if depth_1 < depth_2:
        node_1 = n1
        node_2 = n2
    else:
        node_1 = n2
        node_2 = n1
        depth_1, depth_2 = depth_2, depth_1

    while depth_1 != depth_2:
        node_2 = parent[node_2]
        depth_2 -= 1

    while node_1 != node_2:
        node_1 = parent[node_1]
        node_2 = parent[node_2]

    return str(node_1)


def dfs(tree: list, node: int):
    root = 1
    stack = [root]
    depth = [0] * (node + 1)
    parent = [0] * (node + 1)
    depth[root] = 1
    while stack:
        v = stack.pop()
        for w in tree[v]:
            if not depth[w]:
                depth[w] = depth[v] + 1
                parent[w] = v
                stack.append(w)
    return depth, parent


def main():
    N = int(input())
    tree = insert(N)
    depth, parent = dfs(tree, N)
    M = int(input())
    result = [None] * M
    for i in range(M):
        n1, n2 = map(int, input().split())
        print(LCA(n1, n2, depth, parent) + "\n")


main()