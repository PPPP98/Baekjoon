import sys
input = sys.stdin.readline

N = int(input())
arr = [0] * 10001

for _ in range(N):
    arr[int(input())] += 1

max_w = 0

for i in range(1, 10001):
    if arr[i] == 0: # 없으면 skip
        continue
    else:
        w = 0 # 무게 초기화
        w = N * i # 무게 계산
        if max_w < w: # 최대값 갱신
            max_w = w
        N -= arr[i] # 계산 했던 로프의 개수 제거

print(max_w)