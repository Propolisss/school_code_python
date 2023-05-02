def f(n, base):
    temp = 0
    n = n[::-1]
    for i in range(len(n)):
        temp += int(n[i]) * base ** i
    return temp

for x in range(15):
    n1 = f(f'97968{x}15', 15)
    n2 = f(f'7{x}233', 15)
    if (n1 + n2) % 14 == 0:
        print(x, (n1 + n2) // 14)