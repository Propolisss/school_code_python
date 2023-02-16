def f(x, y):
    return (x < a) or (y < a) or ((x + 2 * y) > 150)

for a in range(3_000):
    if all(f(x, y) for x in range(10000) for y in range(10000)):
        print(a)
        break