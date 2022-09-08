st = input()
print(st[:st.find('h')] + st[st.rfind('h') + 1:])