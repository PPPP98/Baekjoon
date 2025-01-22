import sys

T = int(sys.stdin.readline())

for i in range(T):
    R, S = map(str, sys.stdin.readline().split())
    for j in range(len(S)):
        print(S[j] * int(R), end="")
    print()
