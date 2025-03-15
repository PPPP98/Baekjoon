import sys

input = lambda: sys.stdin.readline().strip()
out = lambda x: sys.stdout.write(x)

T = int(input())

for tc in range(T):
    order = input()
    N = int(input())
    arr = input().strip("[]").split(",")

    if (N - order.count("D")) < 0:
        out("error\n")
        continue

    front = 0
    rear = N - 1
    pivot = True
    for x in order:
        if x == "R":
            pivot = not pivot
        elif x == "D":
            if pivot:
                front += 1
            else:
                rear -= 1

    arr = arr[front : rear + 1]
    if pivot:
        out("[" + ",".join(arr) + "]")
    else:
        arr.reverse()
        out("[" + ",".join(arr) + "]")

    out("\n")
