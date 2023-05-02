st = open('24_7891.txt').readline()
alph = ''
for i in st:
    if i not in alph:
        alph += i
maxx = float('-inf')

for let in alph:
    #print(st.replace(let, ' ' + let).split(), let)
    s = st.replace(let, ' ' + let).split()
    for i in range(len(s) - 1):
        if s[i][0] == s[i + 1][0]:
            maxx = max(maxx, len(s[i]) + 1)
print(maxx)