a = input()
b = input()

if (a == 'красный' or a == 'синий' or a == 'желтый') and (b == 'красный' or b == 'синий' or b == 'желтый'):
    if a == 'красный' and b == 'синий':
        print('фиолетовый')
    if a == 'красный' and b == 'желтый':
        print('оранжевый')
    if a == 'синий' and b == 'желтый':
        print('зеленый')
    if a == b:
        print(a)
else:
    print('ошибка цвета')