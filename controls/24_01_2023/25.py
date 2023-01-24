def div(n):
    dels_ = set()

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            dels_ |= {i, n // i}
    return sorted(dels_)



for i in range(100806, 100950 + 1):
    dels = div(i)
    if len(dels) == 6:
        print(dels[-3], dels[-2])