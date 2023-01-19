def check_num(n):
    dels = set()

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            dels |= {i, n // i}
    return n == sum(dels) / 2

print(check_num(int(input())))