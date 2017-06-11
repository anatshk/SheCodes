"""
https://docs.google.com/document/d/1lnUaaDEBXZLUB6KYQFzK7CVXsVHxx4579iXWqibz8YM/edit
"""


class SudokuCalc:
    """
    Will contain all data and calculation methods.
    """

    board_size = 9

    def __init__(self, filename):
        """
        Initialized Sudoko board from file.
        The file contains 9 rows of 9 characters, characters are 0-9, where 0 indicates the cell is empty.
        :param filename: path to txt file
        """

        self.board = SudokuCalc.create_board(filename)

    @staticmethod
    def create_board(filename):
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

    # TODO: continue from here, part B in link above
    def start(self):
        self.is_game_over = False
        self.start_puzzle = self.board.copy()

    def check_win(self):
        """
        Checks rows, columns, squares for winning conditions - contain all values 1-9, without repeating.
        :return:
        """

    @staticmethod
    def _check_row(row):
        """
        convert row to list and call _check_values
        :param row:
        :return:
        """
        pass

    @staticmethod
    def _check_col(col):
        """
        convert col to list and call _check_values
        :param col:
        :return:
        """
        pass

    @staticmethod
    def _check_square(square):
        """
        convert square to list and call _check_values
        :param square:
        :return:
        """
        pass

    @staticmethod
    def _check_values(value_list):
        """
        Checks if value_list contains all values 1-9, without repeating.
        :param value_list:
        :return:
        """



class SudokuDisplay:
    """
    Will contain all display methods.
    """