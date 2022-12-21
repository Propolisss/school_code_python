def merge(list1, list2):
    merged = []
    left = 0
    right = 0

    for i in range(len(list1) + len(list2)):
        if left < len(list1) and right < len(list2):
            if list1[left] < list2[right]:
                merged.append(list1[left])
                left += 1
            else:
                merged.append(list2[right])
                right += 1
        elif left >= len(list1):
            merged.append(list2[right])
            right += 1
        elif right >= len(list2):
            merged.append(list1[left])
            left += 1
    return merged
n1 = [int(i) for i in input().split()]
n2 = [int(i) for i in input().split()]

print(merge(n1, n2))
