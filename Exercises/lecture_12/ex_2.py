"""
Ex 2:
1. Extend the program in exercise 7 of the loop control statements chapter to include exception handling.

Exercise 7:

Prompt a user for some personal details:

person = {}

for prop in ["name", "surname", "age", "height", "weight"]:
    person[prop] = input("Please enter your %s: " % prop)

Modify the example above to include type conversion of the properties: age should be an integer,
height and weight should be floats, and name and surname should be strings.

Whenever the user enters input of the incorrect type, keep prompting the user for the same value until it
is entered correctly. Give the user sensible feedback.

2. Add a try-except statement to the body of this function which handles a possible IndexError,
which could occur if the index provided exceeds the length of the list. Print an error message if this happens:

def print_list_element(thelist, index):
    print(thelist[index])

3. This function adds an element to a list inside a dict of lists. Rewrite it to use a try-except statement
which handles a possible KeyError if the list with the name provided doesn’t exist in the dictionary yet,
instead of checking beforehand whether it does. Include else and finally clauses in your try-except block:

def add_to_list_in_dict(thedict, listname, element):
    if listname in thedict:
        l = thedict[listname]
        print("%s already has %d elements." % (listname, len(l)))
    else:
        thedict[listname] = []
        print("Created %s." % listname)

    thedict[listname].append(element)

    print("Added %s to %s." % (element, listname))
"""

# 1

def section_1():
    # age should be an integer,
    # height and weight should be floats,
    # name and surname should be strings.

    person = {}


    def get_valid_input(input_str, typecast_function):
        while True:
            try:
                res = typecast_function(input_str)
                break
            except ValueError:
                input_str = input("Try again, we're expecting {}, but we got {}: " .format(typecast_function, input_str))
        return res

    for prop in ["name", "surname", "age", "height", "weight"]:
        input_value = input("Please enter your %s: " % prop)
        if prop == 'age':
            input_value = get_valid_input(input_value, int)
        elif prop in ['height', 'weight']:
            input_value = get_valid_input(input_value, float)
        person[prop] = input_value

    print("full name: {} {}, age: {}, height {}, weight {}".format(*person.values()))

# section_1()

# 2


def section_2():
    def print_list_element(thelist, index):
        try:
            print(thelist[index])
        except IndexError:
            print('Your index ({}) exceeds list length ({})'.format(index, len(thelist)))

    print_list_element([1, 2, 3], 1)
    print_list_element([1, 2, 3], 8)

# section_2()

# 3

def section_3():
    """
    This function adds an element to a list inside a dict of lists. Rewrite it to use a try-except statement
    which handles a possible KeyError if the list with the name provided doesn’t exist in the dictionary yet,
    instead of checking beforehand whether it does. Include else and finally clauses in your try-except block
    :return:
    """
    def add_to_list_in_dict(thedict, listname, element):
        try:
            l = thedict[listname]
        except KeyError:
            thedict[listname] = []
            print("Created %s." % listname)
        else:
            print("%s already has %d elements." % (listname, len(l)))
        finally:
            thedict[listname].append(element)
            print("Added %s to %s." % (element, listname))

    d = {
        'aaa': [1, 2, 3],
        'bbb': [5]
    }
    add_to_list_in_dict(d, 'aaa', 'boom')
    print(d)
    add_to_list_in_dict(d, 'blahblah', 'boom')
    print(d)

section_3()