nums = [i for i in input().split()]
st = '+'.join(nums) + '='
print(st, sum([int(i) for i in nums]), sep='')