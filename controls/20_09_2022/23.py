def f(a, b, count):
    if a > b:
        return 0
    elif a == b and count == 1:
        return 1
    else:
        return f(a + 1, b, count) + f(a + 2, b, count) + f(a * 2, b, count + 1)

print(f(2, 12, 0))