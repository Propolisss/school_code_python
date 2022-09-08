a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if 1 <= a1 <= 8 and 1 <= b1 <= 8 and 1 <= a2 <= 8 and 1 <= b2 <= 8:
    if (abs(a1 - a2) == 2 and abs(b1 - b2) == 1) or (abs(b1 - b2) == 2 and abs(a1 - a2) == 1):
        print('yes')
    else:
        print('no')
else:
    print('no')