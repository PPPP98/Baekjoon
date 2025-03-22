import sys

input = lambda: sys.stdin.readline().strip()


def init(N: int) -> list:
    return [list(map(int, input().split())) for _ in range(N)]


def main():
    N = int(input())
    graph = init(N)

    for k in range(N):
        for i in range(N):
            if graph[i][k]:
                for j in range(N):
                    graph[i][j] = graph[i][j] or graph[k][j]

    for i in range(N):
        print(*graph[i])


if __name__ == "__main__":
    main()
