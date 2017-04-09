def censor(text, word):
    num = len(word)
    ix = text.find(word)
    if ix == -1:
        return text
    while ix != -1:
        text = text[0:ix] + '*' * num + text[(ix+num):]
        ix = text.find(word)
    return text


def median(l):
    if len(l) == 1:
        return l[0]
    l = sorted(l)
    num = len(l)
    if num % 2:
        # odd num of items
        ix = (num - 1) / 2
        med = l[ix]
    else:
        # even num of items
        med = 0.5 * float(l[num/2] + l[num/2 + 1])
    return med

print(median([4, 5, 5, 4]))

