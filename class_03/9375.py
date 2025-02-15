import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    clothes = {}
    for i in range(N):
        name, cate = input().rstrip().split()
        
        if cate not in clothes:
            clothes[cate] = []
        
        clothes[cate].append(name)

    result = 1
    for item in clothes:
        result *= (len(clothes[item]) + 1)
    
    print(result - 1)