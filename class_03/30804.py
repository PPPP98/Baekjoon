import sys

input = sys.stdin.readline

N = int(input())

stick = list(map(int, input().split()))
candy_list = [0] * 10


def check_remain(temp):
    remain = 0
    for candy in temp:
        if candy != 0:
            remain += 1
    return remain

max_candy = 0

front = rear = 0

temp = [0] * 10
check = 0
while True:
    if check > 2:
        temp[stick[front]] -= 1
        front += 1
    else:
        temp[stick[rear]] += 1
        rear += 1
    
    check = check_remain(temp)

    if check <= 2:
        max_candy = max(max_candy, sum(temp))
    
    if  N == rear:
        break

print(max_candy)
