import sys

S = sys.stdin.readline().rstrip()

for i in range(97, 123):
    print(S.find(chr(i)), end=' ')
