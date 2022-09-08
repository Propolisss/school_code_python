import math
a = float(input())
b = float(input())
c = float(input())
d = (b ** 2) - 4 * a * c

if d > 0:
    print((-b + math.sqrt(d)) / 2 * a)
    print((-b - math.sqrt(d)) / 2 * a)
elif d == 0:
    print(-b / 2 * a)
else:
    print('Нет корней')