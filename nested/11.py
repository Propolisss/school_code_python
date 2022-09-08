n = int(input())
summ = 0

def fac(nn):
    if nn == 0:
        return 1
    else:
        return nn * fac(nn - 1)

for i in range(1, n + 1):
    for j in range(1):
        summ += fac(i)
print(summ)