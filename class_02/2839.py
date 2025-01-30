def min_count(num):
    if num == 4 or num == 7:
        return -1
    if num % 5 == 0:
        return num // 5
    if num % 5 == 1:
        return ((num // 5) - 1) + 2
    if num % 5 == 2:
        return ((num // 5) - 2) + 4
    if num % 5 == 3:
        return ((num // 5)) + 1
    if num % 5 == 4:
        return ((num // 5) - 1) + 3


N = int(input())
print(min_count(N))

