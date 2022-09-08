a = int(input())
b = int(input())
c = int(input())

if (a > b and b > c) or (c > b and b > a):
    print(b)
else:
    if (a > c and c > b) or (b > c and c > a):
        print(c)
    else:
        print(a)