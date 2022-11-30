st = open('24-212.txt').readline().replace('C', 'B').replace('D', 'B').replace('O', 'A')
maxx = float('-inf')

for i in range(len(st)):
    j = i + 2
    count = 0
    while j < len(st):
        if st[j - 2:j] == 'AB':
            count += 1
        else:
            maxx = max(maxx, count)
            break
        j += 2
        maxx = max(maxx, count)
print(maxx)
# st = open('24-212.txt').readline()
# gl = 'AO'
# sogl = 'BCD'
# maxx = float('-inf')
#
# for i in range(len(st)):
#     j = i + 2
#     count = 0
#     while j < len(st):
#         if (st[j - 2] in gl) and (st[j - 1] in sogl):
#             count += 1
#         else:
#             maxx = max(maxx, count)
#             break
#         j += 2
#         maxx = max(maxx, count)
# print(maxx)
