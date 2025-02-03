import sys
input = sys.stdin.readline

K = int(input())

num_stack = []
for _ in range(K):
    num = int(input())
    try:
        if num == 0:
            num_stack.pop()
        else:
            num_stack.append(num)
    except IndexError:
        pass

print(sum(num_stack))
