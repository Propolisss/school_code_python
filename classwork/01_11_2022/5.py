nums = []
s = set()


for i in range(1000000):
    n = i
    if i % 3 == 0:
        n //= 3
    else:
        n -= 1

    if n % 5 == 0:
        n //= 5
    else:
        n -= 1

    if n % 11 == 0:
        n //= 11
    else:
        n -= 1

    if n == 8:
        nums.append(i)
        s.add(i)
print(len(nums), len(s))