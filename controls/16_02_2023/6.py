def f(x, y):
    return ((2 * x + 3 * y) != 75) or (a > (3 * x)) or (a > (2 * y))

for a in range(3_000):
    if all(f(x, y) for x in range(10000) for y in range(10000)):
        print(a)
        break