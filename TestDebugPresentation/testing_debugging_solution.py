#######################################################################################################################
# Fixed versions - for slides only
#######################################################################################################################


def return_last_name_fixed(full_name):
    """
    Return the last name from the string 'full_name'.
    Assume that the first, middle and last names are separated by spaces.
    Assume same order: first, middle (optional), last.
    Examples -
    'John Cougar Mellencamp' will return 'Mellencamp',
    'Taylor Swift' will return 'Swift'
    'Madonna' will return 'No last name'
    :param full_name: string, contains full name (first, middle, last) separated by spaces.
    :return: string, last name
    """
    space_indices = [ix for ix, letter in enumerate(full_name) if letter == ' ']

    if len(space_indices) == 0:
        # no spaces were found in 'full_name'
        return 'No last name'
    else:
        # at least one space was found in 'full_name'
        return full_name[space_indices[-1]+1:]


def return_last_name_fixed_one_line(full_name):
    """
    Return the last name from the string 'full_name'.
    Assume that the first, middle and last names are separated by spaces.
    Assume same order: first, middle (optional), last.
    Examples -
    'John Cougar Mellencamp' will return 'Mellencamp',
    'Taylor Swift' will return 'Swift'
    'Madonna' will return 'No last name'
    :param full_name: string, contains full name (first, middle, last) separated by spaces.
    :return: string, last name
    """
    assert full_name.isalpha(), 'The full name contains non-letters. Please try again.'
    assert len(full_name), "Empty string provided. Please try again."

    space_indices = [ix for ix, letter in enumerate(full_name) if letter == ' ']

    return 'No last name' if len(space_indices) == 0 else full_name[space_indices[-1]+1:]

assert return_last_name_fixed_one_line('John Cougar Mellencamp') == 'Mellencamp', 'WRONG for \'John Cougar Mellencamp\''
assert return_last_name_fixed_one_line('Taylor Swift') == 'Swift', 'WRONG for \'Taylor Swift\''
assert return_last_name_fixed_one_line('Madonna') == 'No last name', 'WRONG for \'Madonna\''

return_last_name_fixed_one_line('123 Bob')
return_last_name_fixed_one_line('')