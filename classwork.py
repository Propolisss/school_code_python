


def f(a, b, start, target):
    if (a + b) >= 259: return (start % 2) == (target % 2)
    if start == target: return 0
    h = [f(a + 1, b, start + 1, target), f(a * 2, b, start + 1, target), f(a, b + 1, start + 1, target), f(a, b * 2, start + 1, target)]
    return any(h) if (start + 1) % 2 == target % 2 else all(h)

for s in range(1, 241 + 1):
    if f(17, s, 0, 4):
        print(s)