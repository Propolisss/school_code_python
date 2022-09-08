a = int(input())

if a >= 1 and a < 60:
    print('Легкий вес')
elif a >= 60 and a <= 64:
    print('Первый полусредний вес')
elif a >= 64 and a <= 69:
    print('Полусредний вес')
else:
    print('нет такого веса')