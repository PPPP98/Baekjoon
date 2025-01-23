import sys

L = int(sys.stdin.readline())
str_hash = sys.stdin.readline().rstrip()

result = 0
m = 1234567891
for i in range(L):
    result += (int(ord(str_hash[i])) - ord('a') + 1) * (31 ** i)

print(result % m)