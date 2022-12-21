def get_days(month):
    if month == 2:
        return 28
    elif str(month) in '13578' or month == 10 or month == 12:
        return 31
    else:
        return 30

print(get_days(int(input())))