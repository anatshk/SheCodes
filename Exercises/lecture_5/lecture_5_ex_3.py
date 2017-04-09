def char_freq(string):
    d = {}
    for s in string:
        if s in d.keys():
            d[s] += 1
        else:
            d[s] = 1
    return d


def char_freq2(string):
    d = {}
    for s in set(list(string)):
        d[s] = string.count(s)
    return d

assert char_freq('abzz') == {'a': 1, 'b': 1, 'z': 2}
assert char_freq2('abzz') == {'a': 1, 'b': 1, 'z': 2}
