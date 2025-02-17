import sys
input = sys.stdin.readline

N = int(input())

field = [list(map(int, input().split())) for _ in range(N)]

def count_paper(arr):
    white = blue = 0
    length = len(arr)

    base = arr[0][0]

    for i in range(length):
        for j in range(length):
            if base != arr[i][j]:
                break
        if base != arr[i][j]:
                break
    else:
        if base:
            blue += 1
        else:
            white += 1
        return (white, blue)
    
    temp = []
    for j in range(0, length, length // 2):
        sub_field1 = []
        sub_field2 = []
        for i in range(length // 2):
            sub_field1.append(arr[i][j : (j + (length // 2))])
            sub_field2.append(arr[(length // 2) + i][j : (j + (length // 2))])
        temp.append(sub_field1)
        temp.append(sub_field2)

    for t in temp:
        w, b = count_paper(t)
        white += w
        blue += b
    
    return (white, blue)

white, blue = count_paper(field)
print(f"{white}\n{blue}")
