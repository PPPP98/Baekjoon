import sys
input = sys.stdin.readline

N = int(input())

arr = []
stack_arr = []
push_pop = []
flag = True

for _ in range(N):
    stack_arr.append(int(input()))

stack_idx = 0
arr_idx = 0
top = N
for i in range(1, N + 1):
    arr.append(i)
    push_pop.append("+")
    try:
        while arr[arr_idx] == stack_arr[stack_idx]:
            arr.pop()
            push_pop.append("-")
            arr_idx -= 1
            stack_idx += 1
            if i == top:
                break
    except IndexError:
        pass
    arr_idx += 1

while arr:
    if arr.pop() == stack_arr[stack_idx]:
        push_pop.append("-")
        stack_idx += 1
    else:
        flag = False
        break

if flag and not arr:
    for w in push_pop:
        print(w)
    pass
else:
    print("NO")
