import sys

arr = []
for _ in range(3):
    arr.append(sys.stdin.readline().strip())


for i in range(3):
    if arr[i].isdecimal():
        idx = i
        break

C_value = abs(idx - 3)



def define_fzbz(r):
    if r % 3 == 0:
        if r % 5 == 0:
            return 'FizzBuzz'
        return 'Fizz'
    if r % 5 == 0:
        return 'Buzz'
    return r

print(define_fzbz(int(arr[idx]) + C_value))