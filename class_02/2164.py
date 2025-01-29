from collections import deque

class deck_card:
    def __init__(self, num):
        self.arr_len = num
        self.q_arr = deque(range(1, num + 1))

    def result(self):
        for _ in range(self.arr_len - 1):
            self.q_arr.popleft()
            self.q_arr.append(self.q_arr.popleft())
        return self.q_arr.pop()

N = int(input())
card_arr = deck_card(N)
print(card_arr.result())
