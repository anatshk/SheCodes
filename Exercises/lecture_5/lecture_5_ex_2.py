def foo(list_of_strings):
    total = 0
    for s in list_of_strings:
        if len(s) >=2 and s[0] == s[-1]:
            total += 1
    return total

assert foo(['aba', 'xyz', 'aa', 'x', 'bbb']) == 3
assert foo(['', 'x', 'xy', 'xyx', 'xx']) == 2
