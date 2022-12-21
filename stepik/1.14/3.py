def get_factors(num):
    dels = set()

    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            dels |= {i, num // i}
    return sorted(dels)

print(get_factors(int(input())))