import sys
input = sys.stdin.readline

T = int(input())

def check_VPS(Str):
    Stack_str = []
    for w in Str:
        if w == '(':
            Stack_str.append(w)
        elif w == ')':
            if not Stack_str:
                return 'NO'
            else:
                Str_pop = Stack_str.pop()
                if Str_pop != '(':
                    return 'NO'
    return 'YES' if not Stack_str else 'NO'


for _ in range(T):
    Str = input().strip()
    print(check_VPS(Str))
