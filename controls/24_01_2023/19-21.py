def f(a, count, target):
    if a >= 22: return (count % 2) == (target % 2)
    if count == target: return 0
    h = [f(a + 1, count + 1, target), f(a + 2, count + 1, target), f(a * 2, count + 1, target)]
    return any(h) if (count + 1) % 2 == target % 2 else all(h)


count = 0

for i in range(1, 21 + 1):
    for j in range(2, 100, 2):
        if f(i, 0, j):
            count += 1
            break
print(count)

