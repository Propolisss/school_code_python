st = input()
sound = 'ауоыиэяюёе'
silence = 'бвгджзйклмнпрстфхцчшщ'
count_sound = 0
count_silence = 0
st = st.lower()

for i in range(len(st)):
    if st[i] in sound:
        count_sound += 1
    elif st[i] in silence:
        count_silence += 1
print('Количество гласных букв равно', count_sound)
print('Количество согласных букв равно', count_silence)