def check_pal(num):
    num_str = str(num)
    length = len(num_str)

    for i in range(length//2):
        if num_str[i] != num_str[length - i - 1]:
            return False
    else:
        return True


N = int(input())

num = 2 if N == 1 else N
while True:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        if check_pal(num):
            break
    num += 1

print(num)