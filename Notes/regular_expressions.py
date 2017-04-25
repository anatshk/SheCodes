"""
Regular Expressions (https://www.youtube.com/watch?v=sZyAn2TW7GY)
===================

Identifiers:
\d - any number
\D - anything BUT a number
\s - space
\S - anything But a space
\w - any character
\W - anything BUT a character
. - (period) any character, except for a newline
\. - actual period in text
\b - the white space around words

Modifiers:
{1, 3} - we're expecting 1-3 characters, for example, \d{1-3}
+ - match 1 or more
? - match 0 or 1
* - match 0 or more
$ - match the end of a string
^ - match the beginning of a string
| - either or, for example \d{1,3} | \w{5,6}
[] - range or "variance", for example, [A-Z] will find capital letters, [1-5a-qA-Z] will find any of the 1-5, a-q, A-Z
{x} - expecting exactly x amount

White space characters:
\n - newline
\s - space
\t - tab
\e - escape
\f - form feed
\r - return
mostly used are \n, \s, \t

Special characters that need to be escaped (with \):
. + * ? [ ] $ ^ ( ) { } | \
"""

import re

exampleString = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97 and his grandfather, Oscar, is 102.
'''

# We would like to extract all names and ages from the string, assuming the format "name xxxxxx age"
# Assume - only names are capitalized.

ages = re.findall(r'\d{1,3}', exampleString)  # look for numbers, 1 number, 2 numbers or 3 numbers
names = re.findall(r'[A-Z][a-z]*', exampleString)  # look for anything starting with 1 capital letter followed by any number of lowercase letters

print(ages)
print(names)


"""
Additional info -
https://developers.google.com/edu/python/regular-expressions
"""