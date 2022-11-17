s = [i for i in open('24-164.txt')]

lens = []
dic = dict()
all_dic = dict()
st = ''
maxx_len = float('-inf')

for i in range(len(s)):
    local_max = float('-inf')
    for j in range(len(s[i])):
        if s[i][j] in all_dic:
            all_dic[s[i][j]] += 1
        else:
            all_dic[s[i][j]] = 1
        st = s[i][j]
        k = j + 1

        while k < len(s[i]):
            if st[-1] == s[i][k]:
                st += s[i][k]
                k += 1
            else:
                break
        maxx_len = max(maxx_len, len(st))
        local_max = max(local_max, len(st))
    lens.append(local_max)

row = lens.index(maxx_len)
for i in s[row]:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

maxx_let = ''
maxx_count = float('-inf')

for i in dic:
    if dic[i] > maxx_count:
        if (len(maxx_let) > 0 and i < maxx_let):
            maxx_count = dic[i]
            maxx_let = i
        else:
            maxx_count = dic[i]
            maxx_let = i
print(maxx_let, all_dic[maxx_let], sep='')