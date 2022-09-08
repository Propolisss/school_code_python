a = int(input())

if ((a // 1000) + ((a // 10) % 10)) == ((((a // 100) % 10) + (a % 10))):
    print('Красиво!!')
else:
    print('NO!')