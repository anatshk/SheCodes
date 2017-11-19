"""
This is an example of "test first" flow.
"""

# Task:
# Write a function that a string 's'.
# The function should return the number of vowels in 's'
# if there are more vowels than consonants.
# Otherwise return number of consonants.
# Also, return a string 'vowels' \ 'consonants',
# depending of what is returned.


def count_letters(s):
    """
    Return 'vowels' and number of vowels in 's' if 's'
    has more values than consonants.
    Otherwise return 'consonants' and number of consonants.
    :param s: String
    :return: int - number of letters, str -
             'vowels' \ consonants'
    """

    # TODO: Validate Input! String with at least one character,
    # TODO: letters only.
    # TODO: Remove punctuation marks before starting.
    # TODO: Write this function!

    return number_of_letters, return_string

# Tests
n1, s1 = count_letters('dog')
assert n1 == 2 and s1 == 'consonants', 'Does not work for "dog"'

assert count_letters('ewe') == (2, 'vowels'), 'Fails for "ewe"'

# TODO: test what happens when we enter empty string?
# TODO: string with numbers? string with punctuation?




