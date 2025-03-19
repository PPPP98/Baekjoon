import sys

input = lambda: sys.stdin.readline().strip()


def divide(target):
    res = 0
    for x in arr:
        if x <= target:
            res += x
        else:
            res += target

    if res <= M:
        return True
    else:
        return False


def bin_search():
    start = 1
    end = max(arr)
    while start <= end:
        mid = (start + end) // 2
        if divide(mid):
            start = mid + 1
        else:
            end = mid - 1
    return end


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    M = int(input())
    ans = bin_search()
    sys.stdout.write(str(ans))
