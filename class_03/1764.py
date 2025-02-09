import sys

input = sys.stdin.readline

set1 = set()
set2 = set()

N, M = map(int, input().split())

for _ in range(N):
    set1.add(input().strip())

for _ in range(M):
    set2.add(input().strip())

result = list(set1 & set2)
result.sort()

print(len(result))
print("\n".join(result))
