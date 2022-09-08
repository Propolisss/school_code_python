count = 0
minn = 10000000

def fun(n):
    if (n % 3 == 0 or n % 7 == 0) and (n % 2 != 0 and n % 10 != 0 and n % 14 != 0 and n % 18 != 0):
        return True
    else:
        return False
    
for i in range(1016, 7937 + 1):
    if fun(i):
        if count == 0:
            minn = i
        count += 1
print(count, minn, sep = '')