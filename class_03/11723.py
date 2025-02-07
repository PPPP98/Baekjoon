# 집합 set 구현
# 1 <= x <= 20
import sys
input = sys.stdin.readline

class Set:
    def __init__(self):
        self.S = 0

    def add(self, x):
        self.S = self.S | (1 << (x - 1))

    def remove(self, x):
        self.S = self.S & ~(1 << (x - 1))

    def check(self, x):
        if self.S & (1 << (x - 1)):
            return 1
        else:
            return 0

    def toggle(self, x):
        if self.S & (1 << (x - 1)):
            self.remove(x)
        else:
            self.add(x)

    def all(self):
        self.S = (1 << 20) - 1

    def empty(self):
        self.S = 0
    
    def handle(self, cmd, x = 0):
        x = int(x)
        if cmd == "add":
            self.add(x)
        elif cmd == "remove":
            self.remove(x)
        elif cmd == "check":
            print(self.check(x))
        elif cmd == "toggle":
            self.toggle(x)
        elif cmd == "all":
            self.all()
        elif cmd == "empty":
            self.empty()

N = int(input())

S = Set()

for _ in range(N):
    cmd_line = list(input().split())
    S.handle(*cmd_line)
        
