for i in range(40):
    for j in range(40):
        for k in range(40):
            st = '0' + '1' * i + '2' * j + '3' * k + '0'
            length = len(st)
            while '00' not in st:
                st = st.replace('01', '21022', 1)
                st = st.replace('02', '310', 1)
                st = st.replace('03', '230112', 1)
            if st.count('1') == 104 and st.count('2') == 39 and st.count('3') == 83:
                print(length)