def back(t=0):
    global min_v
    if M > len(select) + (len(chicken) - t):
        return

    if len(select) == M:
        min_v = min(min_v, score())
        return

    for i in range(t, len(chicken)):
        select.append(chicken[i])
        back(i + 1)
        select.pop()


def score():
    board = [float("inf")] * len(house)
    for r, c in select:
        for i in range(len(house)):
            x, y = house[i]
            t = abs(r - x) + abs(c - y)
            board[i] = min(board[i], t)
    return sum(board)


N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

chicken = []
house = []
select = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chicken.append((i, j))
        elif city[i][j] == 1:
            house.append((i, j))

min_v = float("inf")
back()
print(min_v)