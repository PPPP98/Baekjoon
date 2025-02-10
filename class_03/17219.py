import sys
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())

site_dict = {}
for _ in range(N):
    site, password = input().strip().split()
    site_dict[site] = password

for _ in range(M):
    site = input().strip()
    print(f"{site_dict[site]}\n")
