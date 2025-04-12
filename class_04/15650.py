import sys
input = lambda:sys.stdin.readline().strip()

def back(idx):
    if idx > N and len(select) < M:
        return
    if len(select) == M:
        print(*select)
        return
    select.append(idx)
    back(idx + 1)
    select.pop()
    back(idx + 1)

N, M = map(int,input().split())
select = []
back(1)