a = int(input())

if a == 0:
    print('зеленый')
else:
    if a >= 1 and a <= 10:
        if a % 2 == 0:
            print('черный')
        else:
            print('красный')
    if a >= 11 and a <= 18:
        if a % 2 == 0:
            print('красный')
        else:
            print('черный')
    if a >= 19 and a <= 28:
        if a % 2 == 0:
            print('красный')
        else:
            print('черный')
    if a >= 29 and a <= 36:
        if a % 2 == 0:
            print('черный')
        else:
            print('красный')
    if a > 36:
        print('ошибка ввода')