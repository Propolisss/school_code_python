st = input()

print(st[:st.find('h')] + st[st.rfind('h'):st.find('h'):-1] + st[st.rfind('h'):])