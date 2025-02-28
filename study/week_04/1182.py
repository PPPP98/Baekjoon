def find_S(arr, N, S, idx=0, res = 0):
    global cnt
    # 마지막 인덱스
    if idx == N:
        if res == S:
            cnt += 1
        return
    # 탐색
    find_S(arr, N, S, idx + 1, res + arr[idx])
    find_S(arr, N, S, idx + 1, res)


if __name__ == "__main__":
    N, S = map(int, input().split())

    arr = list(map(int, input().split()))
    arr.sort()
    cnt = 0
    find_S(arr, N, S)

    if S == 0:
        cnt -= 1

    print(cnt)
