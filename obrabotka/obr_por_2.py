n = int(input())
nn = ''

while n != 0:
    nn += str(n % 10)
    n //= 10
print(nn)