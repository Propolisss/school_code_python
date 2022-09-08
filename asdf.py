count = 0
x = 0

for i in range(354261000, 354261000 - 944694, -1):
    x = i
    n = 987
    while (x+n)//1000 < 354261:
        x = x - 5
        n = n + 8
    if n//1000 == 231:
        print(i)
        count += 1
print(count)