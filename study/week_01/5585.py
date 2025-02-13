# 500, 100, 50, 10, 5, 1
N = int(input())

change = 1000 - N
cnt = 0
while change != 0:
    if (change // 500) != 0:
        n = change // 500
        change -= n * 500
        cnt += n
    elif (change // 100) != 0:
        n = change // 100
        change -= n * 100
        cnt += n
    elif (change // 50) != 0:
        n = change // 50
        change -= n * 50
        cnt += n
    elif (change // 10) != 0:
        n = change // 10
        change -= n * 10
        cnt += n   
    elif (change // 5) != 0:
        n = change // 5
        change -= (change // 5) * 5
        cnt += n
    elif change != 0:
        n = change
        change -= n
        cnt += n

print(cnt)
