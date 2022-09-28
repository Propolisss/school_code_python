def dels(n):
    all_dels = set()

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            all_dels |= {i, n // i}
    return sorted(all_dels)

n = int(input())

ans = list(dels(n))
print(ans)