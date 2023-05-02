file = open('22_2.txt')
dic = {'0' : 0}
nums = [i.split() for i in file]

while len(dic) < len(nums) + 1:
    for s in nums:
        if all(sub in dic for sub in s[2:]):
            dic[s[0]] = int(s[1]) + max(dic[sub] for sub in s[2:])
print(max(dic.values()))