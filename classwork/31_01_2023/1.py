nums = [i.split() for i in open('22')]
dic = {'0' : 0}
count = 0

while len(dic) < len(nums) + 1:
    for s in nums:
        if all(sub in dic for sub in s[2:]):
            dic[s[0]] = int(s[1]) + max(dic[sub] for sub in s[2:])

for i in dic:
    if dic[i] > 90:
        count += 1
print(count)