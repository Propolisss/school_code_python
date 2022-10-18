count = 0


for i in range(0, 1_000_000 + 2, 2):
    st = oct(i)[2:]
    if len(st) == 5 and st[0] == '7':
        if ('65' in st) ^ ('56' in st):
            count += 1
print(count)