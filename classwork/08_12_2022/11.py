def print_fio(name_, surname_, patronymic_):
    print((surname_[0] + name_[0] + patronymic_[0]).upper())

name = input()
surname = input()
patronymic = input()
print_fio(name, surname, patronymic)