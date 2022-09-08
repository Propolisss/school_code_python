n = int(input())
st = input()
stt = ''

for i in range(len(st)):
    ordd = ord(st[i])
    if 128 - ordd > n:
        if ordd + n < 128:
            stt += chr(ordd + n)
        else:
            stt += chr(ordd - n)
    else:
        if 128 - ordd > 13:
            stt += chr(ordd + (26 - n))
        else:
            stt += chr(ordd - n)
print(stt)