import sys
input = sys.stdin.readline

N = int(input())
wait_t = list(map(int, input().split()))

wait_t.sort()

acm_sum = 0
time_sum = 0
for time in wait_t:
    acm_sum += time
    time_sum += acm_sum

print(time_sum)