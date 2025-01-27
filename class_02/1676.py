import sys

# 팩토리얼 0의 개수는 / 10이 되는 개수 만큼임 2 * 5
# 5의 갯수만 계산하면 됨 이유) 2의 갯수는 5보다 무조건 많음
# 2의 개수

# 5의 개수
def check_5(num):
    count = 0
    while True:
        if num % 5 == 0:
            count += 1
            num /= 5
        else:
            break
    return count
    

N = int(sys.stdin.readline())

count_5 = 0

for i in range(1, N + 1):
    count_5 += check_5(i)

print(count_5)

