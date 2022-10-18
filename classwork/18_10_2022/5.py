nums9 = []
count = 0

def to_nine(n):
    temp_n = n
    temp_st = ''

    while temp_n:
        temp_st = f'{temp_n % 9}{temp_st}'
        temp_n //= 9
    return temp_st

for i in range(1000000):
    nums9.append(to_nine(i))


for st in nums9:
    if len(st) == 5:
        if st[0] not in '13579' and st[-1] not in '18' and st.count('3') <= 1:
            count += 1
print(count)