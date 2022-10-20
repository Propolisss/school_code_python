nums = [int(i) for i in input().split('.')]
flag = 1

for i in nums:
    if i > 255:
        flag = 0
if flag:
    print('ДА')
else:
    print('НЕТ')