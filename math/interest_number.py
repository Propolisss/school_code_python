a = int(input())
n1 = a // 100
n2 = ((a % 100) // 10)
n3 = a % 10

if abs((n1 - n3)) == n2:
    print('Число интересное')
else:
    print('Число неинтересное')