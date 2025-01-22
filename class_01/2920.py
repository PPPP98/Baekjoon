import sys

scale = list(map(int, sys.stdin.readline().split()))


def determine_scale(sc):
    if sc[0] == 1:
        for i in range(8):
            if sc[i] == i + 1:
                pass
            else:
                return "mixed"
        return "ascending"
    elif sc[0] == 8:
        for i in range(8):
            if sc[i] == (8 - i):
                pass
            else:
                return "mixed"
        return "descending"

    else:
        return "mixed"

print(determine_scale(scale))