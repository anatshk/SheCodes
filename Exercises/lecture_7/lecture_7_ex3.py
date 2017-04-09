def fizzbuzz_auto(count_to):
    for num in range(1, count_to+1):
        if num % 7:
            print(num)
            continue
        print('boom')

# fizzbuzz_auto(50)

# ======================================


def fizzbuzz(count_to):
    for num in range(1, count_to+1):
        x = input('Enter next number:')
        if num % 7:
            if int(x) != num:
                print('You are wrong, it was supposed to be {}'.format(num))
                break
        else:
            if x != 'boom':
                print('You are wrong, it was supposed to be "boom"')
                break
    else:
        print('Good Job!')

# fizzbuzz(20)

# =======================================================================================


def computer_turn(num):
    if not num % 14:
        return 'splat'
    elif not num % 7:
        return 'boom'
    return num


def user_turn(num):
    x = input('User turn. Enter next number:')
    if not num % 14:
        if x != 'splat':
            return False
    elif not num % 7:
        if x != 'boom':
            return False
    else:
        if isinstance(x, str) or int(x) != num:
            return False
    return True


def fizzbuzz_2_players(count_to):
    is_user_turn = False

    for num in range(1, count_to + 1):
        if is_user_turn:
            was_user_correct = user_turn(num)
            if not was_user_correct:
                print('Wrong, it was supposed to be {}'.format(computer_turn(num)))
                break
        else:
            print('Computer turn: {}'.format(computer_turn(num)))
        is_user_turn = not is_user_turn

fizzbuzz_2_players(15)