a = int(input())
b = int(input())
c = input()
if c != '+' or c != '-' or c != '*' or c != '/':
    if c == '/' and b == 0:
        print('На ноль делить нельзя!')
    else:
        if c == '*':
            print(a * b)
        elif c == '+':
            print(a + b)
        elif c == '-':
            print(a - b)
        elif c == '/':
            print(a / b)
else:
    print('Неверная операция')