def f(start, end, last):
    if start > end:
        return 0
    elif start == end:
        return 1
    else:
        if last == '+3':
            return f(start + 1, end, '+1') + f(start * 2, end, last + '*2')
        else:
            return f(start + 1, end, '+1') + f(start + 3, end, '+3') + f(start * 2, end, last + '*2')
print(f(2, 20, ''))