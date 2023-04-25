st = open('24_3792.txt').readline().replace('A', '*').replace('B', '*').replace('C', '*').replace('D', ' ').replace('E', ' ')
print(max(len(i) for i in st.split()))