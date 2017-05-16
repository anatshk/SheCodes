"""
Helper file to figure out patterns for baby names exercise
"""

import re

text = '<h3 align="center">Popularity in 1990</h3>'
pattern = r'Popularity in (\d{4})<'
year = re.findall(pattern, text)

text = """
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
"""
pattern = r'>(\d+)</td><td>(\w+)</td><td>(\w+)<'
names_ranks = re.findall(pattern, text)
male_names = {}
female_names = {}
for rank, male, female in names_ranks:
    male_names[male] = int(rank)
    female_names[female] = int(rank)

all_names = female_names
all_names.update(male_names)
names_sorted = sorted(all_names.keys())
list_final = year
for name in names_sorted:
    # TODO: continue building the list
    list_final.append('{} {}'.format(name, all_names[name]))
    pass
a=5