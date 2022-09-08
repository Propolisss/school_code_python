a = int(input())
b = int(input())
k1 = 0
k2 = 0

if a - 2 != 0 and b - 1 != 0:
    k1 = k1 + 1
elif b - 2 != 0 and a - 1 != 0:
    k2 = k2 +1
    print(k1, k2)
else:
    print(-1)