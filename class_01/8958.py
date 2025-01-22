import sys

T = int(sys.stdin.readline())

for _ in range(T):
    result = sys.stdin.readline().rstrip()
    score = 0
    stack = 1
    for i in range(len(result)):
        if result[i] == 'O':
            score += stack
            stack += 1
        else:
            stack = 1
    print(score)

