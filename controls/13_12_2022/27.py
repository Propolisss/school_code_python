file = open('27b (1).txt')
n = int(file.readline())

nums1 = [[] for i in range(5)]
nums2 = [[] for i in range(5)]
maxx_diff = float('-inf')

for i in range(n):
    n1, n2 = map(int, file.readline().split())
    if n1 > n2:
        nums1[n1 % 5].append(n1)
        nums2[n2 % 5].append(n2)
    else:
        nums1[n1 % 5].append(n2)
        nums2[n2 % 5].append(n1)
    summ1 = 0
    summ2 = 0
    for i in range(len(nums1)):
        summ1 += sum(nums1[i])
    for i in range(len(nums2)):
        summ2 += sum(nums2[i])
    if abs(summ1 - summ2) % 5 == 0:
        maxx_diff = max(maxx_diff, abs(summ1 - summ2))
print(maxx_diff)