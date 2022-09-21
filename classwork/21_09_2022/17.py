with open('17-335.txt') as file:
    nums = [int(i) for i in file]
minn = 10 ** 10
nn = []

for i in range(len(nums)):
    if nums[i] % 43 == 0:
        minn = min(minn, nums[i])

count1 = 0
count2 = 0
count3 = 0
mcount1 = 0
mcount2 = 0
mcount3 = 0
ans = []
count = 0

for i in range(1, len(nums)):
    if ((nums[i - 1] + nums[i]) % minn == 0):
        count1 += 1
    if (str(nums[i - 1])[-1] == '7'):
        count2 += 1
    if (str(nums[i])[-1] == '7'):
        count3 += 1
    if ((nums[i - 1] + nums[i]) % minn == 0) or (str(nums[i - 1])[-1] == str(minn)[-1]) or (str(nums[i])[-1] == str(minn)[-1]):
        count += 1
    if ((nums[i - 1] + nums[i]) % minn == 0 and str(nums[i - 1])[-1] == '7'):
        mcount1 += 1
    if ((nums[i - 1] + nums[i]) % minn == 0 and str(nums[i])[-1] == '7'):
        mcount2 += 1
    if ((nums[i - 1] + nums[i]) % minn == 0 and str(nums[i - 1])[-1] == '7' and str(nums[i])[-1] == '7'):
        mcount3 += 1
    if ((nums[i - 1] + nums[i]) % minn == 0 and str(nums[i - 1])[-1] == '7' and str(nums[i])[-1] != '7'):
        mcount3 += 1
    if ((nums[i - 1] + nums[i]) % minn == 0 and str(nums[i - 1])[-1] != '7' and str(nums[i])[-1] == '7'):
        mcount3 += 1

print(count1, count2, count3, count1 + count2 + count3 - mcount1 - mcount2 - mcount3)
print(count)