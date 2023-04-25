def f(a, b, count, target):
    if (a + b) >= 245: return (count % 2) == (target % 2)
    if count == target: return 0
    h = [f(a + 1, b, count + 1, target), f(a * 2, b, count + 1, target), f(a, b + 1, count + 1, target), f(a, b * 2, count + 1, target)]
    return any(h) if (count + 1) % 2 == target % 2 else all(h)

for i in range(1, 224 + 1):
    if not(f(15, i, 0, 2)) and f(15, i, 0, 4):
        print(i)