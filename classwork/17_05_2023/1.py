file = open('27B_7881.txt')
n = int(file.readline())
k = int(file.readline())
k37 = [0] * 100
n37 = [0] * 100
nums = [int(i) for i in file]
count = 0

for i in range(k + 1):
    print(i)
    if nums[i] % 37 == 0:
        k37[nums[i] % 100] += 1
    else:
        n37[nums[i] % 100] += 1

    for j in range(i + 1, k + 1):
        if abs(nums[i] - nums[j]) % 100 == 0 and ((nums[i] % 37 == 0) ^ (nums[j] % 37 == 0)):
            count += 1

left = -1
right = k
for i in range(n - k - 1):
    left += 1
    right += 1
    #print(i, left, right, count, nums[left + 1 : right + 1], nums[left], nums[right])
    n1 = nums[left]
    n2 = nums[right]
    if n1 % 37 == 0:
        k37[n1 % 100] -= 1 if k37[n1 % 100] > 0 else 0
    else:
        n37[n1 % 100] -= 1 if n37[n1 % 100] > 0 else 0

    if n2 % 37 == 0:
        count += n37[n2 % 100]
    else:
        count += k37[n2 % 100]

    if n2 % 37 == 0:
        k37[n2 % 100] += 1
    else:
        n37[n2 % 100] += 1
print(count)