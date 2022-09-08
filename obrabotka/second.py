n = int(input())

while n != 0:
    if n < 100:
        print(n % 10)
        break
    n //= 10