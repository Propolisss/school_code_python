def prod(n):
    pr = 1
    for i in str(n):
        pr *= int(i)
    return pr


def f(start, end):
    if start == end:
        return 1
    elif start < 10:
        return 0
    else:
        return f(sum(int(i) for i in str(start)), end) + f(prod(start), end)


count = 0

for i in range(10, 99 + 1):
    if f(i, 8):
        count += 1
print(count)