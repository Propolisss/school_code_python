def f(s, count, target):
    if s >= 2200: return (count % 2) == (target % 2)
    if count == target: return 0
    h = [f(s + 2, count + 1, target), f(s + 3, count + 1, target), f(s * 2, count + 1, target)]
    return any(h) if (count + 1) % 2 == target % 2 else all(h)

print('19)', [i for i in range(1, 2199 + 1) if f(i, 0, 2)])
print('20)', [i for i in range(1, 2199 + 1) if not f(i, 0, 1) and f(i, 0, 3)])
print('21)', [i for i in range(1, 2199 + 1) if not f(i, 0, 2) and f(i, 0, 4)])