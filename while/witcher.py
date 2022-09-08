n = int(input())
count = 0
k = 0

while n != 0:
    k += n // 25
    n -= 25 * k
    count += k
    k = 0
    k += n // 10
    n -= 10 * k
    count += k
    k = 0
    k += n // 5
    n -= 5 * k
    count += k
    k = 0
    k += n // 1
    n -= 1 * k
    count += k
    k = 0
print(count)