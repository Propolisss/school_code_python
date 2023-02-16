def f(x):
    B = 70 <= x <= 80
    return (x % 12 == 0) and B and (x % a != 0)

ans = set()
for a in range(1, 10_000):
    if all(f(x) == 0 for x in range(1, 100_000)):
        ans.add(a)
print(len(ans))