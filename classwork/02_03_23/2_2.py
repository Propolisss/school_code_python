minn = float('inf')

for x in range(1_000):
    for y in range(1_000):
        if all(i in '01234567' for i in str(x)) and all(i in '01234567' for i in str(y)):
            n1 = f'36{x}53'
            n2 = f'4{y}3'
            if int(n1, 8) - int(n2, 8) > 0:
                minn = min(minn, int(n1, 8) - int(n2, 8))
print(minn)