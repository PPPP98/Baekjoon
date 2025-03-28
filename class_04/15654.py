def back(idx):
  if idx == M:
    print(*choice)
    return
  for i in range(N):
    if not select[i]:
      select[i] = True
      choice.append(arr[i])
      back(idx + 1)
      choice.pop()
      select[i] = False


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
select = [False] * N
choice = []
back(0)