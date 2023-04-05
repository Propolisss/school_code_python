def f(x):
    return (x % a == 0) or ((50 <= x <= 70) <= (not(x % 16 == 0)))

for a in range(1, 10_000):
    if all(f(x) for x in range(1, 10_000)):
        print(a)