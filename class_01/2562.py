list_num = []
for i in range(9):
    list_num.append(int(input()))

max_list = max(list_num)

print(max_list)
print(list_num.index(max_list) + 1)
