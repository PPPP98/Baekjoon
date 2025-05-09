import sys

input = lambda: sys.stdin.readline()
sys.setrecursionlimit(12000)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class bintree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
            return
        else:
            node = self.root
            self._insert(node, data)

    def _insert(self, node: Node, data: int):
        if data > node.data:
            if node.right == None:
                node.right = Node(data)
            else:
                self._insert(node.right, data)
        else:
            if node.left == None:
                node.left = Node(data)
            else:
                self._insert(node.left, data)

    def postorder(self):
        def _postorder(node: Node):
            if node.left != None:
                _postorder(node.left)
            if node.right != None:
                _postorder(node.right)
            res.append(str(node.data))

        res = []
        _postorder(self.root)
        print("\n".join(res))


if __name__ == "__main__":
    tree = bintree()
    try:
        while True:
            tree.insert(int(input()))
    except:
        pass

    tree.postorder()
