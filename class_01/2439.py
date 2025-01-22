import sys

"""
    *
   **
  ***
 ****
*****
"""
N = int(sys.stdin.readline())
for i in range(N):  # 0 1 2 3 4
    for j in range(N - i - 1):  # 0 1 2 3
        print(" ", end="")
    for j in range(i + 1):  # 0
        print("*", end="")
    print()
