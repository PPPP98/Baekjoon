import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())

arr = []
stack_arr = []
push_pop = []
flag = True


stack_arr = [int(input()) for _ in range(N)]

stack_idx = 0
top = N
for i in range(1, N + 1):
    arr.append(i)
    push_pop.append("+")

    while arr[-1] == stack_arr[stack_idx]:
        arr.pop()
        push_pop.append("-")
        stack_idx += 1
        if i == top or not arr:
            break

while arr:
    if arr.pop() == stack_arr[stack_idx]:
        push_pop.append("-")
        stack_idx += 1
    else:
        flag = False
        break

if flag and not arr:
    print("\n".join(push_pop))
    pass
else:
    print("NO")
