N = int(input())

def check_pal(num):
    num_str = str(num)
    length = len(num_str)

    for i in range(length//2):
        if num_str[i] != num_str[length - i - 1]:
            return False
    else:
        return True

max_num = 1000000
num_list = [True for _ in range(1000001)]
num_list[0] = False
num_list[1] = False

for i in range(2, int(max_num ** 0.5) + 1):
    if num_list[i]:
        j = i * i
        while j <= max_num:
            num_list[j] = False
            j += i
    else:
        continue

prime_list = [x for x in range(max_num + 1) if num_list[x]]

prime_list.append(1003001)
for num in prime_list:
    if num >= N:
        if check_pal(num):
            print(num)
            break


