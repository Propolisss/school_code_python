def to_base(n, base):
    temp_n = n
    arr = []

    while temp_n:
        arr = [temp_n % base] + arr
        temp_n //= base
    return arr

num = 3 *15 ** 1140 + 2 * 15 ** 1025 + 15 ** 923 - 3 * 15 ** 85 + 2 * 15 ** 74 + 3
nums = to_base(num, 15)
count = 1
maxx = float('-inf')

for i in range(len(nums) - 1):
    if nums[i + 1] == nums[i]:
        count += 1
        maxx = max(maxx, count)
    else:
        count = 1
print(maxx)