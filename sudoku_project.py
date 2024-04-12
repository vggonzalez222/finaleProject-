class SudokuGenerator:
    def __init__(self, row_length=9, removed_cells=30):
        self.row_length = row_length
        self.removed_cells = removed_cells

    def get_board(self):
        list_2d = [[0] * self.row_length for i in range(self.row_length)]
        return list_2d

    def print_board(self):
        board = self.get_board()
        for i in board:
            print(i)
        pass

    def valid_in_row(self, row, num):
        pass

    def valid_in_col(self, col, num):
        pass

    def valid_in_box(self, row_start, col_start, num):
        pass

    def is_valid(self, row, col, num):
        pass

    def fill_box(self, row_start, col_start):
        pass

    def fill_diagonal(self):
        pass

    def fill_remaining(self, row, col):
        pass

    def fill_values(self):
        pass

    def remove_cells(self):
        pass

    def generate_sudoku(self, size, removed):
        pass


test = SudokuGenerator()
test.print_board()
