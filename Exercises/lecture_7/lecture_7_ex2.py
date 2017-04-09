

def foo_low_high(random_num):
    x = int(input('Select a number between 1 and 10: '))
    while x != random_num:
        if x < random_num:
            print("Oh No! You Lost, it's higher")
        elif x > random_num:
            print("Oh No! You Lost, it's lower")
        x = int(input('Try Again: Select a number between 1 and 10: '))
    else:
        print("You Won")

foo_low_high(5)
