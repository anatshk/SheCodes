full_name = 'Bob Marley Jr'


l1 = [ix for ix, letter in enumerate(full_name) if letter == ' ']


l2 = []
for ix, letter in enumerate(full_name):
    if letter == ' ':
        l2.append(ix)

d = {
    'Taylor Swift': 'Swift',
    'Bob Marley': 'Marley',
    'Prince': 'no last name'
}

for input, expected in d.items():
    # assert return_last_name(input) == expected, 'WRONG for {}'.format(input)
    assert return_last_name(input) == expected, 'WRONG for %s' % input

debug_here = 6