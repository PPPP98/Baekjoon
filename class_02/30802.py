N = int(input())
list_size = list(map(int, input().split()))
T, P = map(int, input().split())

T_sh = 0
for i in range(6):
    T_sh += (list_size[i] // T)
    if list_size[i] % T:
        T_sh += 1

print(f'{T_sh}\n{N // P} {N % P}')