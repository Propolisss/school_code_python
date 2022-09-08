a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())

if a1 < b1 and a2 < b2:
    if a2 > b1:
        print(b1, a2)
    elif b1 == a2:
        print(a2)
    else:
        print('пустое множество')
else:
    print('пустое множество')