count = 0
k = 1 / (3 ** 0.5)

for x in range(-176, 1):
    for y in range(-89, 170):
        if (y >= k * x) and (y <= -k * x + 300):
            count += 1
print(count)
print(count - 38879)

