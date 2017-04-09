from random import randint

rand_num = randint(0, 10)


def foo(random_num):
    # x = raw_input('Select a number between 1 and 10: ')
    x = input('Select a number between 1 and 10: ')
    if int(x) == random_num:
        print("You Won")
    else:
        print("Oh No! You Lost, it was {}".format(random_num))

# # check function works with known "random"
# foo(5)
# foo(5)
# # check actual random number
# foo(rand_num)


def wrapper():
    r_num = randint(0, 10)
    foo(r_num)


def foo_low_high(random_num):
    # x = raw_input('Select a number between 1 and 10: ')
    x = input('Select a number between 1 and 10: ')
    if int(x) < random_num:
        print("Oh No! You Lost, it was higher ({})".format(random_num))
    elif int(x) > random_num:
        print("Oh No! You Lost, it was lower ({})".format(random_num))
    else:
        print("You Won")

# check function works with known "random"
foo_low_high(5)
foo_low_high(5)
foo_low_high(5)
# check actual random number
foo_low_high(rand_num)



