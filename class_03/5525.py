import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
string = input().strip()

res = "I" + ("OI" * N)
length = 1 + (2 * N)

def lps(pattern, length):
    lps = [0] * length
    i = 1
    j = 0

    while i < length:
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp(pattern, length, string):
    cnt = 0
    new_lps = lps(pattern, length)

    i = j = 0

    while i < M:
        if string[i] == pattern[j]:
            i += 1
            j += 1

        if j == length:
            cnt += 1
            j = new_lps[j - 1]
        elif i < M and string[i] != pattern[j]:
            if j != 0:
                j = new_lps[j - 1]
            else:
                i += 1
    
    return cnt


print(kmp(res, length, string))