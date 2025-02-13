import sys
input = sys.stdin.readline

def bin_search(arr, size, num):
    if num < arr[0] or num > arr[-1]:
        return 0
    start = 0
    end = size - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == num:
            return 1
        elif arr[mid] > num:
            end = mid - 1
        elif arr[mid] < num:
            start = mid + 1
    
    return 0

N = int(input())
arr = list(map(int, input().split()))

M = int(input())
ch_l = list(map(int, input().split()))

arr.sort()

for n in ch_l:
    print(bin_search(arr, N, n))
