# def to_base(n, base):
#     temp_n = n
#     arr = []
#
#     while temp_n:
#         arr = [temp_n % base] + arr
#         temp_n //= base
#     return arr
#
#
# count = 0
# for i in range(1, 1_000_000):
#     n = to_base(i, 7)
#     if len(n) == 5:
#         if n.count(6) == 1 and (sum(j for j in n if j % 2 == 0) < sum(j for j in n if j & 1)):
#             count += 1
#
# print(count)


# from itertools import *
#
# s = list(map(''.join, permutations("карпы")))
# gl = 'аы'
# sogl = 'крп'
# count = 0
#
# for comb in s:
#     if comb[0] != "р" and comb[-1] != "р":
#         count += 1 if all(comb[i + 1] not in gl for i in range(len(comb) - 1) if comb[i] in gl) else 0
#
# print(count)


def to_base(n, base):
    temp_n = n
    arr = []

    while temp_n:
        arr = [temp_n % base] + arr
        temp_n //= base
    return arr

count = 0
for i in range(1, 100_000_00):
    n = to_base(i, 42)
    if n.count(6) == 1:
        if n[n.index(6) + 1] % 2 != 1 and n[n.index(6) - 1] % 2 != 1:
            count += 1