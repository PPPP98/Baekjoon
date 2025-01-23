import sys

N = int(sys.stdin.readline())


def search(num):
    for i in range(1, num):
        sum = i
        j = i
        while j:
            sum += j % 10
            j = int(j / 10)
        if sum == num:
            return i
    return 0

print(search(N))