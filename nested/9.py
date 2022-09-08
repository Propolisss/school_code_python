n = int(input())
count = 0

for i in range(1, n + 1):
    count = 0
    for j in range(1, int(i ** 0.5) + 1):
        if i % j == 0:
            count += 2
    if i // j == j:
        count -= 1
    print(str(i) + '+' * count)