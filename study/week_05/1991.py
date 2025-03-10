import sys
input = lambda:sys.stdin.readline().rstrip()
print = lambda x:sys.stdout.write(x)


def preorder(tree, p):
    left = tree[p][0]
    right = tree[p][1]
    print(p)
    if left != ".":
        preorder(tree, left)
    if right != ".":
        preorder(tree, right)


def inorder(tree, p):
    left = tree[p][0]
    right = tree[p][1]
    if left != ".":
        inorder(tree, left)
    print(p)
    if right != ".":
        inorder(tree, right)


def postorder(tree, p):
    left = tree[p][0]
    right = tree[p][1]
    if left != ".":
        postorder(tree, left)
    if right != ".":
        postorder(tree, right)
    print(p)


def main():
    N = int(input())
    tree = {}
    for _ in range(N):
        p, l, r = input().split()
        tree[p] = (l, r)
    preorder(tree, "A")
    print("\n")
    inorder(tree, "A")
    print("\n")
    postorder(tree, "A")
    print("\n")

main()
    