def convert_to_python_case(text):
    s = []
    temp_st = text[0]

    for i in range(1, len(text)):
        if text[i].islower() or text[i].isdigit():
            temp_st += text[i]
        else:
            s.append(temp_st.lower())
            temp_st = text[i]
    if len(temp_st) != 0:
        s.append(temp_st.lower())
    return s

print(*convert_to_python_case(input()), sep='_')