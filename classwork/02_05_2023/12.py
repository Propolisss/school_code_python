def f(start, end):
    if start < end:
        return 0
    elif start == end:
        return 1
    num = 0
    num += f(start - 3, end)
    num += f(start // 3, end) if start % 2 == 0 else 0
    num += f(start // 10, end) if len(str(start)) >= 2 else 0
    return num
print(f(1250, 20))