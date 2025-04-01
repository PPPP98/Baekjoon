"""
N개의 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
고른 수열은 비내림차순이어야 한다.
길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.
"""

import sys

input = lambda: sys.stdin.readline().strip()


def back(idx, cnt):
    if idx == L:
        return
    if cnt == M:
        print(*select)
        return

    for i in range(idx, L):
        select.append(arr[i])
        back(i, cnt + 1)
        select.pop()


N, M = map(int, input().split())
arr = sorted(set(map(int, input().split())))
L = len(arr)
select = []
back(0, 0)
