nums = [float(i.replace(',', '.')) for i in open('18.txt')]
maxx = float('-inf')

for i in range(len(nums)):
    summ = nums[i]
    last = nums[i]
    for j in range(i + 1, len(nums)):
        if abs(nums[j] - last) >= 16:
            summ += nums[j]
            last = nums[j]
            maxx = max(maxx, summ)
        else:
            break
        maxx = max(maxx, summ)
print(maxx)