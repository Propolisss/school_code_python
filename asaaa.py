def f(start, end):
    if start > end:
        return 0
    if start == 15 or start == 35:
        return 0
    if start == end:
        return 1
    else:
        return f(start + 1, end) + f(start * 2, end) + f(start ** 2, end)


print(f(5, 69) * f(69, 154))