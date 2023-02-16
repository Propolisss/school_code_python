def f(x):
    return (x % a != 0) <= ((x % 6 == 0) <= (x % 4 != 0))

ans = set()

for a in range(1, 10_000):
    if all(f(x) for x in range(1, 100_000)):
        ans.add(a)
print(max(ans))