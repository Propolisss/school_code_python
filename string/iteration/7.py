st = input()
nums = '1234567890'
flag = 0

for i in range(len(st)):
    if st[i] in nums:
        flag = 1
if flag:
    print('Цифра')
else:
    print('Цифр нет')