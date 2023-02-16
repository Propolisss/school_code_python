p = {48, 52, 56}

def f(x):
    Q = 29 <= x <= 47
    P = x in p
    return ((x % 3 != 0) and (not P)) <= ((abs(x - 50) <= 7) <= Q) or (x & a == 0)

for a in range(1, 1_000):
    if all(f(x) for x in range(10000)):
        print(a)
        break