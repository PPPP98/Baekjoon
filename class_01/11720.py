import sys

N = int(sys.stdin.readline())
num = sys.stdin.readline().strip()
sum = 0

for i in range(len(num)):
    sum += int(num[i])

print(sum)