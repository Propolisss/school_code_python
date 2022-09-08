import math
n = int(input())
summ = 1

for i in range(2, n + 1):
    i **= -1
    summ += i
print(summ - math.log(n))