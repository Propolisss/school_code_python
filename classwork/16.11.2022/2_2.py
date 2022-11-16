def div(n):
    dels = set()

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dels |= {i, n // i}

    return dels

count = 0

for i in range(800_000, 1_000_000):
    summ = sum(div(i))
    pr = 1
    for j in div(i): pr *= j

    if summ & 1 and pr & 1:
        if len(div(i)) > 10:
            print(i, len(div(i)))
            count += 1
    if count == 6:
        break