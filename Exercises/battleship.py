from random import randint


def init_board(size):
    board = []
    for x in range(size):
        board.append(["O"] * size)
    return board


def print_board(board):
    for row in board:
        print(" ".join(row))


def random_row_col(board):
    return randint(0, len(board) - 1)


def play_board(board, turns, ship_row, ship_col):
    for turn in range(turns):
        print("Turn", turn + 1)
        guess_row = int(input("Guess Row:"))
        guess_col = int(input("Guess Col:"))
        if guess_row == ship_row and guess_col == ship_col:
            print("Congratulations! You sunk my battleship!")
            break
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                print("Oops, that's not even in the ocean.")
            elif board[guess_row][guess_col] == "X":
                print("You guessed that one already.")
            else:
                print("You missed my battleship!")
                board[guess_row][guess_col] = "X"
            # Print (turn + 1) here!
            print_board(board)
        if turn == turns - 1:
            print('Game Over')
    return board

################################################################################

print("Let's play Battleship!")
board = init_board(5)
ship_row = random_row_col(board)
ship_col = random_row_col(board)

play_board(board=board, turns=3, ship_row=ship_row, ship_col=ship_col)

# OPTIONAL - add more ships by making ship_row, ship_col a list and making sure the ships din't overlap
# OPTIONAL - make it a 2 player game by initializing 2 boards and calling them one at a time with different boards
#            and turn = 1. In this case, allow for max_turns and do not print game over after each turn.



