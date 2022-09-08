a = int(input())

if (a % 10) == 0 or (5 <= (a % 10) <= 10):
    print(a, 'шоколадок')
if a == 1 or a == 21 or a == 31 or a == 41:
    print(a, 'шоколадка')
if (2 <= (a % 10) <= 4):
    print(a, 'шоколадки')