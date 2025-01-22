while True:
    N = input()
    if N == "0 0 0":
        break
    else:
        A = list(map(int, N.split()))
        A.sort()
        if (A[2]**2) == ((A[0]**2) + (A[1]**2)):
            print("right")
        else:
            print("wrong")
