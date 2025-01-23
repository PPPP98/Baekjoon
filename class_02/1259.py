while True:
    N = input()

    if N == '0' or N[0] == '0':
        break
    if len(N) >= 2:
        for i in range(len(N) // 2):
            if N[i] != N[(- i) - 1]:
                print('no')
                break
            if i + 1 == len(N) // 2:
                print('yes')
                break
    else:
        print('yes')

