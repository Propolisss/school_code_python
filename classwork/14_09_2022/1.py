

count = 0
sq = 2 ** 0.5

for x in range(-400, 400):
    for y in range(-400, 400):
        if (y > -x) and (y < -x + 800 + 40 * sq) and (y > x - 400) and (y < x + 40 * sq + 400) and ((y > 0) and (y < 40 * sq + 400)) and ((x > -20 * sq) and (x < 20 * sq)):
            count += 1
print(count)