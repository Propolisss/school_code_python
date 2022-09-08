a = int(input())
b = int(input())
summ = 0
maxx = 0
summ_maxx = 0

for i in range(a, b + 1):
    summ = 0
    for j in range(1, int(i ** 0.5) + 1):
        if i % j == 0:
            summ += j
            if i // j != j:
                summ += i // j
    if summ > summ_maxx:
        maxx = i
        summ_maxx = summ
print(maxx, summ_maxx)