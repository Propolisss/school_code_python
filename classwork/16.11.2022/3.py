s = []
lens = []

for i in open('24-164.txt'):
    s.append(i)

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

for i in range(len(s)):
    if lens[i] == maxx_len:
        for j in s[i]:
            if j in dic:
                dic[j] += 1
            else:
                dic[j] = 1
        break

maxx_let = ''
maxx_count = float('-inf')

for i in dic:
    if dic[i] > maxx_count:
        maxx_count = dic[i]
        maxx_let = i
print(maxx_let, all_dic[maxx_let])


