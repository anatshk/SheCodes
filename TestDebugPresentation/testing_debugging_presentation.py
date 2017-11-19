"""
This code is for the Testing and Debugging presentation.
https://docs.google.com/presentation/d/1PhPiBiNGhVRb5LUIt4F55hbqVkHpCcb4fXo1zMyedEM/edit?usp=sharing
"""

#######################################################################################################################
# Reminder - Functions
#######################################################################################################################


def function_name(input_name):
    """
    This is the documentation of what this function does.
    :param input_name: This is a description of input to this
           function.
    :return: This is a description of the output of this function.
    """

    # Here we will have code that does whatever the function is
    # supposed to do.
    output_name = input_name  # This is placeholder code
    return output_name

#######################################################################################################################
# Does my function work?  (Work on this code during the presentation)
#######################################################################################################################


def return_last_name(full_name):
    """
    Return the last name from the string 'full_name'.
    Assume that the first, middle and last names are
    separated by spaces.
    Assume same order: first, middle (optional), last.
    Examples -
    'John Cougar Mellencamp' will return 'Mellencamp',
    'Taylor Swift' will return 'Swift'
    'Madonna' will return 'No last name'
    :param full_name: string, contains full name
           (first, middle, last) separated by spaces.
    :return: string, last name
    """
    space_indices = [ix for ix, letter in enumerate(full_name)
                     if letter == ' ']

    if len(space_indices) == 0:
        # no spaces were found in 'full_name'
        print('No last name')
    else:
        # at least one space was found in 'full_name'
        return full_name[space_indices[-1]:]

# intuitive - print result
if return_last_name('John Cougar Mellencamp') == 'Mellencamp':
    print('Correct for \'John Cougar Mellencamp\'')
else:
    print('WRONG for \'John Cougar Mellencamp\'')

# pythonic - assertions
assert return_last_name('Taylor Swift') == 'Swift', \
    'WRONG for \'Taylor Swift\''
assert return_last_name('Madonna') == 'No last name', \
    'WRONG for \'Madonna\''
# assert return_last_name('John Cougar Mellencamp') == 'Mellencamp', 'WRONG for \'John Cougar Mellencamp\''


