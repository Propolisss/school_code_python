def is_correct_bracket(st):
    stack = []

    for i in st:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0 or stack[-1] != '(':
                return False
            del stack[-1]
    if len(stack) != 0:
        return False
    return True

print(is_correct_bracket(input()))