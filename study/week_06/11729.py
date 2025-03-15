import sys
input = lambda:sys.stdin.readline().strip()
out = lambda x:sys.stdout.write(x)

def hanoi(n, start, end):
    if n == 1:
        ans.append(f"{start} {end}")
        return
    way = 6 - start - end
    hanoi(n - 1, start, way)
    ans.append(f"{start} {end}")
    hanoi(n - 1, way, end)

ans = []

N = int(input())
hanoi(N, 1, 3)
out(str(2 ** N - 1) + "\n")
out("\n".join(ans))