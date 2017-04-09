"""
This is an example of Debug Mode.
"""

my_number = 7
my_string = "Hello"
my_dict = {'today': 'Sunday', 'this_year': 2017}


def add_to_dict(d, num, string):
    d['num'] = num
    d['greeting'] = string * 2
    return d

my_dict = add_to_dict(my_dict, my_number, my_string)

print("Finished!")


