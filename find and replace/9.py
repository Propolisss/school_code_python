num = int(input())
count = 0

for i in range(num):
    st = input()
    if st.count('11') >= 3:
        count += 1
print(count)