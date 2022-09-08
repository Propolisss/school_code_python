def fun(n):
    if n == 1:
        return 1
    else:
        if n & 1:
            return 3 * n + fun(n - 2)
        else:
            return 4 * fun(n // 2)
print(fun(42))