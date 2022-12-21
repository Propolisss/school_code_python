def number_of_fators(num):
    dels = set()

    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            dels |= {i, num // i}
    return len(dels)

print(number_of_fators(int(input())))