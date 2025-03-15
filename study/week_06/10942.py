import sys

input = lambda: sys.stdin.readline().strip()
print = lambda x: sys.stdout.write(x)


def question(dp: list):
    M = int(input())
    ans = []
    for _ in range(M):
        s, e = map(int, input().split())
        ans.append(dp[s - 1][e - 1])
    print("\n".join(ans))


def make_dp_table():
    N = int(input())
    arr = tuple(map(int, input().split()))

    dp = [["0"] * N for _ in range(N)]

    dp[N - 1][N - 1] = "1"
    for i in range(N - 1):
        if arr[i] == arr[i + 1]:
            dp[i][i + 1] = "1"
        dp[i][i] = "1"

    for end in range(2, N):
        for start in range(end - 1):
            if arr[start] == arr[end] and dp[start + 1][end - 1] == "1":
                dp[start][end] = "1"

    return dp


if __name__ == "__main__":
    dp_table = make_dp_table()
    question(dp_table)
