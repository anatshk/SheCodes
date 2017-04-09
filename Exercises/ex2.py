from datetime import datetime


def foo():
    # first_name = raw_input('Enter first name: ')
    # surname = raw_input('Enter surname: ')
    # year_of_birth = raw_input('Enter year of birth (4 digits): ')
    first_name = input('Enter first name: ')
    surname = input('Enter surname: ')
    year_of_birth = input('Enter year of birth (4 digits): ')
    initials = first_name[0].upper() + surname[0].upper()
    age_years = int(datetime.now().year) - int(year_of_birth)
    print("your initials are {} and you are {} years old".format(initials, age_years))

foo()