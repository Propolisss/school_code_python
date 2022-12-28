def is_palindrome(text):
    s = []
    for i in text.strip():
        if i not in ' ,.!?-':
            s.append(i.lower())
    for i in range(len(s)):
        if s[i] != s[-i - 1]:
            return False
    return True

print(is_palindrome(input()))