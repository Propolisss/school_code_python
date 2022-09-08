n = int(input())
summ = 0

for i in range(1, n + 1):
    i **= 2
    if i % 10 == 2 or i % 10 == 5 or i % 10 == 8:
        i **= 1/2
        summ += i
print(int(summ))