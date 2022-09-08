n = int(input())
f1 = 1
f2 = 1
f = 0
fib = ''

if n == 1:
    print(1)
elif n == 2:
    print(1, 1)
else:
    for i in range(2, n):
        f = f1 + f2
        f1 = f2
        f2 = f
        fib += str(f) + ' '
    print(1, 1, fib)