def f(x, y):
    return ((x + y) <= 22) or (y <= (x - 6)) or (y >= a)

for a in range(10_000):
    if all(f(x, y) for x in range(2000) for y in range(2000)):
        print(a)