a = int(input())
b = int(input())
c = int(input())
if ((a < b + c) and (b < a + c) and (c < a + b)):
    if (a == b and a == c and b == c):
        print('Равносторонний')
    else:
        if a == b and b != c:
            print('Равнобедренный')
        else:
            print('Разносторонний')
else:
    print('Не существует такого треугольника')