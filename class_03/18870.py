import sys
input = sys.stdin.readline

N = int(input())

num = list(map(int, input().split()))

pos_dict = {}


for cnt, n in enumerate(sorted(set(num))):
    pos_dict[n] = cnt

result = [str(pos_dict[n]) for n in num]

print(" ".join(result))
