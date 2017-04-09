from random import choice
from string import ascii_lowercase


def bulls_ans_cows(real, guess):
    """
    Bull - correct letter in correct position.
    Cow - correct letter in wrong position.
    :param real: 5-letter string
    :param guess: 5-letter string
    :return: bulls, cows - number of bulls and cows, integers.
    """
    assert len(real) == len(guess), \
        'guess length mismatch. real string is {}-letter long, wile guess is {}-letter long'.format(len(real), len(guess))
    bulls = sum([r == g for r, g in zip(real, guess)])
    total_matching_letters = sum([g in real for g in guess])
    return bulls, total_matching_letters - bulls

# test cases for bulls_ans_cows
assert bulls_ans_cows('abcd', 'acdz') == (1, 2)
assert bulls_ans_cows('abcd', 'abdz') == (2, 1)


def game(str_length=5, debug_input=None):
    if debug_input:
        real = debug_input
    else:
        # generate random string
        real = ''
        for i in range(str_length):
            real += choice(ascii_lowercase)

    # ask user to start playing
    print("Let's play Bulls and Cows")

    win = False
    while not win:
        # user input
        guess = input("Enter your guess: ")
        if guess == 'QUIT':
            # stop condition for debugging
            break
        # get number of bulls and cows
        b, c = bulls_ans_cows(real, guess)
        # check win condition
        if b == len(real):
            win = True
        else:
            print("Incorrect, {} Bulls, {} Cows, Try again!".format(b, c))
    else:
        print("You Win!")

game(debug_input='hello')





