import sys
input = sys.stdin.readline

def cut_tree(high : int):
    cut_sum = 0
    for x in tree:
        if x > high:
            cut_sum += (x - high)
    #print(cut_sum)

    if cut_sum >= M:
        return True
    else:
        return False


N, M = map(int, input().split())
tree = list(map(int, input().split()))

start = 1
end = max(tree)

while start <= end:
    mid = (start + end) // 2
    
    if cut_tree(mid):
        start = mid + 1
    else:
        end = mid - 1
    
print(end)