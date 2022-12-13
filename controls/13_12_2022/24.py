st = open('24.txt').readline()

for i in '0123456789':
    st = st.replace(i, ' ')

s = []

for i in range(len(st)):
    j = i + 1
    temp_st = ''
    while j < len(st):
        if st[j].isalpha():
            temp_st += st[j]
        else:
            if len(temp_st) != 0:
                s.append(temp_st)
            break
        j += 1

maxx_len = float('-inf')
for i in s:
    maxx_len = max(maxx_len, len(i))
print(maxx_len, s)