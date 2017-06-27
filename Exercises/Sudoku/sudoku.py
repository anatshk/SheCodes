"""
https://docs.google.com/document/d/1lnUaaDEBXZLUB6KYQFzK7CVXsVHxx4579iXWqibz8YM/edit
"""

from math import sqrt
from tkinter import *

# Constants
MARGIN = 20  # pix around the board
SIDE = 50  # width of board cell
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # board width and height


class SudokuCalc:
    """
    Will contain all data and calculation methods.
    """

    board_size = 9

    def __init__(self, filename):
        """
        Initialized Sudoku board from file.
        The file contains 9 rows of 9 characters, characters are 0-9, where 0 indicates the cell is empty.
        :param filename: path to txt file
        """

        self.start_puzzle = SudokuCalc.create_board(filename)

    @staticmethod
    def create_board(filename):
        """
        Board is represented by a list of lists, each inner list is a row in the filname.
        :param filename:
        :return:
        """
        f = open(filename, 'r')
        txt = f.read()
        f.close()

        rows = txt.split('\n')
        assert len(rows) == SudokuCalc.board_size, \
            'Unsupported column length {}, expected column length is {}.'.format(len(rows), SudokuCalc.board_size)

        def str_to_list(s):
            l = []
            for char in s:
                assert char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], \
                    'Unsupported character \'{}\'. Only digits 0-9 are supported'.format(char)
                l.append(int(char))
            return l

        board = []
        for row_str in rows:
            row = str_to_list(row_str)
            assert len(row) == SudokuCalc.board_size, \
                'Unsupported row length {}, expected row length is {}.'.format(len(row), SudokuCalc.board_size)
            board.append(row)
        return board

    def start(self):
        self.is_game_over = False
        self.board = self.start_puzzle.copy()

    def check_win(self):
        """
        Checks rows, columns, squares for winning conditions - contain all values 1-9, without repeating.
        If all are correct - set gameover flat to True, return True, otherwise return False
        :return:
        """
        # go over rows
        rows_ok = []
        for row in self.board:
            rows_ok.append(SudokuCalc._check_row(row))

        # go over columns
        cols_ok = []
        cols = self._extract_cols()
        for col in cols:
            cols_ok.append(SudokuCalc._check_row(col))

        # go over squares
        squares_ok = []
        squares = self._extract_squares()
        for square in squares:
            squares_ok.append(SudokuCalc._check_row(square))

        return all(rows_ok) and all(cols_ok) and all(squares_ok)

    def _extract_cols(self):
        """
        Extracts columns from self.board to list of lists, where each inner list is a column of the board.
        :return:
        """
        return [[row[ix] for row in self.board] for ix in range(self.board_size)]

    def _extract_squares(self):
        """
        Extracts squares from self.board to list of lists, where each inner list is a square in the board.
        :return:
        """
        num_row_in_square = int(sqrt(self.board_size))

        # separate board into lists of n values - rows of squares.
        # The order of squares from board is top-to-bottom, left-to-right, starting with top-left square
        col_squares = [[row[ix:ix + num_row_in_square] for row in self.board] for ix in
                       range(0, self.board_size, num_row_in_square)]

        # collect squares and flatten them
        flat_squares = []
        for col in col_squares:
            for ix in range(0, self.board_size, num_row_in_square):
                square = col[ix:ix + num_row_in_square]
                flat_squares.append([item for sublist in square for item in sublist])
        return flat_squares


    @staticmethod
    def _check_row(row):
        """
        convert row to list and call _check_values
        :param row:
        :return:
        """
        return SudokuCalc._check_values(row[:])

    @staticmethod
    def _check_col(col):
        """
        convert col to list and call _check_values
        :param col:
        :return:
        """
        pass  # this is not needed. we can extract columns into lists (rows)

    @staticmethod
    def _check_square(square):
        """
        convert square to list and call _check_values
        :param square:
        :return:
        """
        return SudokuCalc._check_values([val for row in square for val in row])

    @staticmethod
    def _check_values(value_list):
        """
        Checks if value_list contains all values 1-9, without repeating.
        :param value_list: list of values
        :return: True \ False
        """
        assert len(value_list) == SudokuCalc.board_size
        return sorted(value_list) == list(range(1, 10))


class SudokuDisplay(Frame):
    """
    Will contain all display methods.
    """

    def __init__(self, parent, filename):
        self.game = SudokuCalc(filename)
        super(SudokuDisplay, self).__init__(master=parent)
        self.parent = parent
        self._initUI()

    def _initUI(self):
        self.parent.title('Sudoku')  # set parent title to 'Sudoku'
        self.pack()  # pack self (current board) to parent
        self.canvas = Canvas(self.parent, height=HEIGHT, width=WIDTH, bg='white')  # add 'canvas' widget using WIDTH and HEIGHT
        self.canvas.pack()  # pack the canvas

        # Create a 'clear' button, bind to self._clear_answers, pack
        self.button_clear_screen = Button(self.parent, text='Clear', command=self._clear_answers)
        self.button_clear_screen.pack()

        self._draw_grid()  # TODO: implement this below
        self._draw_puzzle()  # TODO: implement this below

    def _clear_answers(self):
        # TODO: implement this - see part H
        pass

    def _draw_grid(self):
        """
        Draws grid divided by blue lines into 3x3 squares. Blue lines on square borders, gray lines within squares.
        """
        # TODO: implement this, use canvas.create_line(x0, y0, x1, y1, fill=color)
        # TODO: use WIDTH, HEIGHT, SIDE, MARGIN

        pass

    def _draw_puzzle(self):
        """
        Fills in the cells based on self.game
        """
        # TODO: implement this - see part G


    # TODO: continue from part I

