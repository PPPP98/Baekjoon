string = list(input().split('-'))

sum_list = []
for w in string:
    temp = w.split('+')
    sum_t = 0
    for t in temp:
        sum_t += int(t)
    sum_list.append(sum_t)

result = 0
for i in range(len(sum_list)):
    if i == 0:
        result += sum_list[i]
    else:
        result -= sum_list[i]

print(result)