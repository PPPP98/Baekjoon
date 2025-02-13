N = int(input())
# N <= 1000

result = 0
if N <= 99:
    result = N
else:
    result += 99
    for i in range(100, N + 1):
        num_list = []
        num = i
        while num != 0:
            num_list.append(num % 10)
            num //= 10
        
        if (num_list[0] - num_list[1]) == (num_list[1] - num_list[2]):
            result += 1

if N == 1000:
    result -= 1
        
print(result)