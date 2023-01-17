def f(start, end, last):
    if start > end or start == 6:
        return 0
    elif start == end:
        return 1
    else:
        if last == 1:
            return f(start + 3, end, 3) + f(start ** 2, end, 22)
        elif last == 3:
            return f(start + 1, end, 1) + f(start ** 2, end, 22)
        elif last == 22:
            return f(start + 1, end, 1) + f(start + 3, end, 3)
        else:
            return f(start + 1, end, 1) + f(start + 3, end, 3) + f(start ** 2, end, 22)

print(f(1, 5, 0) * f(5, 25, 0) - 2)