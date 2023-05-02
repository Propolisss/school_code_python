file = open('22_1.txt')
dic = {'0' : 0}
nums = [i.split() for i in file]

while len(dic) < len(nums) + 1:
    for s in nums:
        if all(sub in dic for sub in s[2:]):
            if s[-1] == '0' and len(s) == 3:
                dic[s[0]] = int(s[1]) + max(dic[sub] for sub in s[2:])
            else:
                dic[s[0]] = int(s[1]) + max(dic[sub] for sub in s[2:]) + 20
print(max(dic.values()))