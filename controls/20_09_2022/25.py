def dels(n):
    count_dels = set()

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if (n // i) % 2 == 0:
                count_dels.add(n // i)
            if (i % 2 == 0):
                count_dels.add(i)
    return count_dels

for i in range(190201, 190260 + 1):
    nums = list(dels(i))
    nums.sort()
    if len(nums) == 4:
        print(nums[-1], nums[-2])
