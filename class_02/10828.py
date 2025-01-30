import sys

input = sys.stdin.readline
output = sys.stdout.write  # 더 빠른 출력을 위해 사용


class Stack:
    def __init__(self):
        self.arr = []
        self.top_idx = -1

    def push(self, num):
        self.arr.append(num)
        self.top_idx += 1

    def pop(self):
        if self.top_idx == -1:
            output("-1\n")
        else:
            output(f"{self.arr.pop()}\n")
            self.top_idx -= 1

    def size(self):
        output(f"{len(self.arr)}\n")

    def empty(self):
        output("1\n" if self.top_idx == -1 else "0\n")

    def top(self):
        if self.top_idx == -1:
            output("-1\n")
        else:
            output(f"{self.arr[self.top_idx]}\n")

    def handle(self, command):
        parts = command.split()
        cmd = parts[0]

        if cmd == "push":
            self.push(int(parts[1]))
        elif cmd == "pop":
            self.pop()
        elif cmd == "size":
            self.size()
        elif cmd == "empty":
            self.empty()
        elif cmd == "top":
            self.top()


# 입력 처리
N = int(input().strip())
stack = Stack()

for _ in range(N):
    stack.handle(input().strip())
