st = open('24-186.txt').readline()
nums = []

i = 0
count = 0

while i < len(st):
    if all(j.isdigit() for j in st[i : i + 11]):
        nums.append(st[i : i + 11])
        i += 11
    else:
        i += 1

for i in nums:
    if i[0] == '7' and (int(i[-1]) + int(i[-2]) == int(i[0]) + int(i[1])):
        count += 1
print(count)