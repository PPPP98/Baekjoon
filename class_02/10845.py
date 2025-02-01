import sys
input = sys.stdin.readline

class Que:
    def __init__(self, len_max):
        self.que_size = len_max
        self.que_arr = [None] * len_max
        self.front = self.rear = 0

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return self.front == (self.rear + 1) % self.que_size

    def push(self, data):
        if self.is_full():
            return
        self.rear = (self.rear + 1) % self.que_size
        self.que_arr[self.rear] = data

    def pop(self):
        if self.is_empty():
            print(-1)
        else:
            self.front = (self.front + 1) % self.que_size
            print(self.que_arr[self.front])

    def size(self):
        print((self.rear - self.front + self.que_size) % self.que_size)

    def empty(self):
        if self.is_empty():
            print(1)
        else:
            print(0)
    
    def pfront(self):
        if self.is_empty():
            print(-1)
        else:
            print(self.que_arr[self.front + 1])
    
    def back(self):
        if self.is_empty():
            print(-1)
        else:
            print(self.que_arr[self.rear])

    def handle(self, command):
        data = command.split()
        cmd = data[0]
        if cmd == "push":
            self.push(int(data[1]))
        elif cmd == "pop":
            self.pop()
        elif cmd == "size":
            self.size()
        elif cmd == "empty":
            self.empty()
        elif cmd == "front":
            self.pfront()
        elif cmd == "back":
            self.back()

N = int(input())
new_que = Que(N)

for _ in range(N):
    command = input().strip()
    new_que.handle(command)
