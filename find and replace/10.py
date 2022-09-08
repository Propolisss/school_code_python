st = input()
nums = '0123456789'
count = 0

for i in range(len(st)):
    if st[i] in nums:
        count += 1
print(count)