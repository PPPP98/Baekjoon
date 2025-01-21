import sys

N = 28
list_s = [0 for i in range(N)]
mc = 1

for i in range(N):
    list_s[i] = int(sys.stdin.readline())

list_s.sort()

for i in range(N):
    if mc != list_s[i]:
        print(mc)
        mc += 1
    mc += 1

#29 30 일때 출력안함
