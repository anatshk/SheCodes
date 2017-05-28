a = 'abc'
b = 'abc'

for ix in range(min(len(a), len(b))):
    first_pair = a[ix:ix+2]
    second_pair = b[ix:ix+2]
