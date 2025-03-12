def find_Z(power, r, c, result=0):
    if power == 0:
        return result
    
    next_power = power - 1
    step = 0
    half_idx = 2**next_power
    if r >= half_idx:
        r -= half_idx
        step += 2
    if c >= half_idx:
        c -= half_idx
        step += 1

    result += (step * (half_idx**2))
    return find_Z(next_power, r, c, result)


N, r, c = map(int, input().split())
print(find_Z(N, r, c))