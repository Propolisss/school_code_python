n = int(input())
summ = 0
summ_2 = 0
summ_3 = 0

while n > 0:
    summ += n % 10
    n //= 10
    if n == 0:
        while summ > 0:
            summ_2 += summ % 10
            summ //= 10
            if summ == 0:
                    while summ_2 > 0:
                        summ_3 += summ_2 % 10
                        summ_2 //= 10
print(summ_3)