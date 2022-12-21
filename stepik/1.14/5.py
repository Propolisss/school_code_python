def find_all(target, symbol):
    symbols = []

    for i in range(len(target)):
        if target[i] == symbol:
            symbols.append(i)
    return symbols

print(find_all(input(), input()))