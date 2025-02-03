# 통계학
import sys

input = sys.stdin.readline


def custom_round(num):
    integer_part = int(num)
    decimal_part = abs(num - integer_part)

    if decimal_part >= 0.5:
        return integer_part + (1 if num > 0 else -1)
    else:
        return integer_part


class PrintAverage:
    def __init__(self, arr, N):
        self.arr = sorted(arr)
        self.N = N

    def arth_avg(self):
        return custom_round(sum(self.arr) / self.N)

    def median(self):
        return self.arr[self.N // 2]

    def frequency_value(self):
        count_dict = {}
        for n in self.arr:
            if n not in count_dict:
                count_dict[n] = 1
            else:
                count_dict[n] += 1
        
        count_list = []
        high_fre = max(count_dict.values())
        for k, v in count_dict.items():
            if high_fre == v:
                count_list.append(k)
        
        if len(count_list) >= 2:
            return count_list[1]
        else:
            return count_list[0]

    def min_max_range(self):
        return self.arr[-1] - self.arr[0]

    def print_info(self):
        info = f"""{self.arth_avg()}
{self.median()}
{self.frequency_value()}
{self.min_max_range()}
"""
        print(info)


N = int(input())
arr = []

for _ in range(N):
    arr.append(int(input()))

avg = PrintAverage(arr, N)

avg.print_info()
