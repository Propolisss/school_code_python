def is_one_away(word1, word2):
    if len(word1) == len(word2):
        count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count += 1
                if count > 1:
                    return False
    if count:
        return True
    return False

print(is_one_away(input(), input()))