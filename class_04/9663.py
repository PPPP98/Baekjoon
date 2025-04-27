d = ((1, 1), (1, 0), (1, -1))

def back(row):
    global cnt
    if row == N:
        cnt += 1
        return

    for col in range(N):
        if ((col not in check) and (row + col not in right_check) and (row - col not in left_check)):
            check.add(col)
            right_check.add(row + col)
            left_check.add(row - col)
            back(row + 1)
            check.remove(col)
            right_check.remove(row + col)
            left_check.remove(row - col)
            

N = int(input())
cnt = 0

check = set()
right_check = set()
left_check = set()

back(0)
print(cnt)