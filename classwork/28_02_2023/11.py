count = 0
ch = '0246'

for i in range(1, 1_000_000):
    n = oct(i)[2:]
    if len(n) == 6:
        if all(n[0] < j and n[1] < j for j in n[2:]) and all(not(n[j - 1] in ch and n[j] in ch and n[j + 1] in ch) for j in range(1, 5)):
            count += 1
print(count)