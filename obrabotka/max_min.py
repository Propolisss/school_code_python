n = int(input())
max = 0
min = 1000000
nn = ''

while n != 0:
    nn = n % 10
    n //= 10
    if nn > max:
        max = nn
    if nn < min and nn <= max:
        min = nn
    nn = 0
print('Максимальная цифра равна', max)
print('Минимальная цифра равна', min)