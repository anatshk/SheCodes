movie = ['The Notebook', 'Maleficent', 'Batman v Superman', 'Black Swan',
         'Gone Girl', 'War of the Worlds', 'Just Married']
actor = ['Rachel McAdams', 'Angelina Jolie', 'Gal Gadot', 'Natalie Portman',
         'Rosamund Pike', 'Dakota Fanning', 'Britanny Murphy']

# EX 1
l1 = ['{} is played by {}'.format(m, a) for m, a in zip(movie, actor)]

# EX 2
d2 = {m: a for m, a in zip(movie, actor)}

# EX 3
l3 = ['{} is played by {}'.format(k, v) for k, v in d2.items()]

# EX 4
l4 = [x * 100 for x in range(1, 10) if not (x % 2)]

# EX 5
l5 = [x * 100 if not (x % 2) else x for x in range(1, 10)]

# EX 6
l6 = ['boom' if not (x % 7) else x for x in range(1, 100)]

# EX 7
sum7 = lambda x, y: x + y

# EX 8
joules = [5000, 8000, 10000, 6000, 12000]
j_to_kcal = 4184
l8 = [(j, j / j_to_kcal) for j in joules]

# EX 9
l9 = [(a, b) for a in range(1, 7) for b in range(1, 7)]

# EX 10
languages = ["HTML", "JavaScript", "Python", "Ruby"]
l10 = list(filter(lambda x: x == 'Python', languages))