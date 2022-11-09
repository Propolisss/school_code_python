def dels(n):
    all_dels = set()

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            all_dels.add(i)
            all_dels.add(n // i)
    return sorted(all_dels)


for i in range(100806, 100950 + 1):
    d = dels(i)
    if len(d) == 6:
        print(*(d[-3:-1]), d)