s = []
maxx = 0


file = open('24-171.txt')
for i in file:
    s.append(i[:-2].replace('XYZ', '*'))


for i in range(len(s)):
    temp_st = ''
    j = 0
    previous = 0
    while j < len(s[i]):
        temp_st = ''
        j = previous
        while j < len(s[i]) and s[i][j] in 'XYZ*':
            temp_st += s[i][j]
            if s[i][j] in 'XYZ' and len(temp_st) > 1:
                j += 1
                break
            j += 1
        previous += 1
        temp_st = temp_st.replace('*', 'XYZ')
        maxx = max(maxx, len(temp_st))
print(maxx)