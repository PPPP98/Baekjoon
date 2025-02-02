import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
card_list = list(input().split())
M = int(input())
int_list = list(input().split())

card_table = dict()
for n in card_list:
    if n not in card_table:
        card_table[n] = 1
    else:
        card_table[n] += 1

for n in int_list:
    print(f'{card_table.get(n, 0)} ')
