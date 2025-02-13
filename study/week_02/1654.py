"""
랜선을 모두 N개의 같은 길이의 랜선으로 만들고 싶었기 때문에
K개의 랜선을 잘라서 만들어야 한다.

300cm 짜리 랜선에서 140cm 짜리 랜선을 두 개 잘라내면 20cm는 버려야 한다.

K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없다고 가정

자를 때는 항상 센티미터 단위로 정수길이만큼 자른다

N개보다 많이 만드는 것도 N개를 만드는 것에 포함

최대 랜선의 길이를 구하는 프로그램을 작성

1 <= K <= 10,000     # 가지고 있는 선의 수
1 <= N <= 1,000,000  # 필요한 개수

K <= N

4 11
802
743
457
539

가능한 해 -> X

X * N + C = sum(wire)

* C = 자르고 남은 와이어

X 를 찾는 문제

이론상 최대 가능한 X => sum(wire) // N

1 ~ max(X) 의 range 에서 가능한 최대 값을 찾는 문제 -> 정렬된 정수에서 탐색 -> 이분탐색
"""

import sys

input = sys.stdin.readline

K, N = map(int, input().split())

wire = [int(input()) for _ in range(K)]

sum_w = sum(wire)

max_x = sum_w // N

start = 1
end = max_x

while start <= end:
    X = (start + end) // 2

    C = 0
    for w in wire:
        C += w % X

    if sum_w < (X * N) + C:
        end = X - 1
    else:
        start = X + 1

print(end) # 