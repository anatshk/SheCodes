from Exercises.Sudoku.sudoku import SudokuCalc

# ====================================== Test Create Board ======================================

# sanity
fname = 'sudoku_example.txt'
board = SudokuCalc.create_board(fname)
expected_board = [
    [2, 1, 0, 0, 0, 0, 4, 0, 0],
    [3, 8, 0, 4, 0, 0, 7, 0, 2],
    [0, 0, 0, 7, 2, 0, 0, 0, 0],
    [0, 2, 4, 8, 0, 6, 9, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 2, 0, 3, 5, 4, 0],
    [0, 0, 0, 0, 5, 8, 0, 0, 0],
    [9, 0, 3, 0, 0, 4, 0, 2, 8],
    [0, 0, 8, 0, 0, 0, 0, 5, 7]
]

assert board == expected_board, 'create board function does not work as expected'

# incorrect data
try:
    board = SudokuCalc.create_board('sudoku_bad_example_1_columns.txt')
except AssertionError as e:
    assert e.args[0] == 'Unsupported column length 10, expected column length is 9.'

try:
    board = SudokuCalc.create_board('sudoku_bad_example_2_rows.txt')
except Exception as e:
    assert e.args[0] == 'Unsupported row length 10, expected row length is 9.'

try:
    board = SudokuCalc.create_board('sudoku_bad_example_3_values.txt')
except Exception as e:
    assert e.args[0] == 'Unsupported character \'a\'. Only digits 0-9 are supported'


# ====================================== Test Check Win ======================================

assert SudokuCalc._check_values([1, 2, 3, 4, 5, 6, 7, 8, 9])
assert not SudokuCalc._check_values([2, 2, 3, 4, 5, 6, 7, 8, 9])
assert not SudokuCalc._check_values([2, 2, 3, 4, 5, 6, 0, 8, 9])

assert SudokuCalc._check_row([1, 2, 3, 4, 5, 6, 7, 8, 9])
assert not SudokuCalc._check_row([1, 2, 3, 4, 0, 6, 7, 8, 9])

assert SudokuCalc._check_col([[1], [2], [3], [4], [5], [6], [7], [8], [9]])
assert not SudokuCalc._check_col([[1], [2], [3], [4], [0], [6], [7], [8], [9]])

assert SudokuCalc._check_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
assert not SudokuCalc._check_square([[1, 2, 3], [4, 0, 6], [7, 8, 9]])

# TODO: take known solutions from: http://elmo.sbs.arizona.edu/sandiway/sudoku/examples.html