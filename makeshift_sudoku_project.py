<<<<<<< HEAD
import math
import random


class SudokuGenerator:
    def __init__(self, row_length: int, removed_cells: int):
        self.removed_cells = removed_cells
        self.row_length = row_length
        self.board = [[0] * self.row_length for _ in range(row_length)]  # initializes board to be generated
        self.box_length = int(math.sqrt(row_length))  # must be integer to avoid TypeError

    def get_board(self):
        return self.board

    def print_board(self):
        board = self.get_board()  # uses get_board to obtain an empty
        for i in board:
            print(i)
        pass

    def valid_in_row(self, row, num):  # returns True is num is in a row already
        if num in self.board[row]:
            return False
        else:
            return True

    def valid_in_col(self, col, num):  # returns True if num is in a column already
        for row in self.board:
            if num == row[col]:
                return False
        else:
            return True

    def valid_in_box(self, row_start, col_start, num):
        for row in self.board[row_start:row_start + 3]:  # splices the first 2D lists (or box) in the active board
            for col in row[col_start:col_start + 3]:  # splices the first three elements inside the list to create box
                if num == col:  # if the inputted number is equal to any number for col, it will return True
                    return False
        else:
            return True  # returns false, indicating the number is not inside the box

    def is_valid(self, row, col, num):
        if not self.valid_in_row(row, num):
            return False
        else:
            if not self.valid_in_col(col, num):
                return False
            else:
                row = row // 3 * 3
                col = col // 3 * 3
                if not self.valid_in_box(row, col, num):
                    return False
                return True

    def fill_box(self, row_start, col_start):
        lib = [i for i in range(1, 10)]  # shuffles the library, effectively making placement random
        random.shuffle(lib)
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                self.board[row][col] = lib.pop(0)  # iterates through the boss and turns it into a number
        pass

    def fill_diagonal(self):
        for i in range(0, 7, 3):
            self.fill_box(i, i)
        pass

    def fill_remaining(self, row, col):  # will find out later on why this is not working as intended!
        if col >= self.row_length and row < self.row_length - 1:
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):  # fill the all the boxes
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)
        pass

    def remove_cells(self):
        counter = self.removed_cells
        while counter != 0:
            i, j = random.randint(0, 8), random.randint(0, 8)  # chooses a random coordinate on the board
            if self.board[i][j] != 0:
                self.board[i][j] = 0
                counter -= 1
            else:
                continue
        pass


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    solution = [row[:] for row in sudoku.board]
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board, solution
=======
import math
import random


class SudokuGenerator:
    def __init__(self, row_length: int, removed_cells: int):
        self.removed_cells = removed_cells
        self.row_length = row_length
        self.board = [[0] * self.row_length for _ in range(row_length)]  # initializes board to be generated
        self.box_length = int(math.sqrt(row_length))  # must be integer to avoid TypeError

    def get_board(self):
        return self.board

    def print_board(self):
        board = self.get_board()  # uses get_board to obtain an empty
        for i in board:
            print(i)
        pass

    def valid_in_row(self, row, num):  # returns True is num is in a row already
        if num in self.board[row]:
            return False
        else:
            return True

    def valid_in_col(self, col, num):  # returns True if num is in a column already
        for row in self.board:
            if num == row[col]:
                return False
        else:
            return True

    def valid_in_box(self, row_start, col_start, num):
        for row in self.board[row_start:row_start + 3]:  # splices the first 2D lists (or box) in the active board
            for col in row[col_start:col_start + 3]:  # splices the first three elements inside the list to create box
                if num == col:  # if the inputted number is equal to any number for col, it will return True
                    return False
        else:
            return True  # returns false, indicating the number is not inside the box

    def is_valid(self, row, col, num):
        if not self.valid_in_row(row, num):
            return False
        else:
            if not self.valid_in_col(col, num):
                return False
            else:
                row = row // 3 * 3
                col = col // 3 * 3
                if not self.valid_in_box(row, col, num):
                    return False
                return True

    def fill_box(self, row_start, col_start):
        lib = [i for i in range(1, 10)]  # shuffles the library, effectively making placement random
        random.shuffle(lib)
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                self.board[row][col] = lib.pop(0)  # iterates through the boss and turns it into a number
        pass

    def fill_diagonal(self):
        for i in range(0, 7, 3):
            self.fill_box(i, i)
        pass

    def fill_remaining(self, row, col):  # will find out later on why this is not working as intended!
        if col >= self.row_length and row < self.row_length - 1:
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):  # fill the all the boxes
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)
        pass

    def remove_cells(self):
        counter = self.removed_cells
        while counter != 0:
            i, j = random.randint(0, 8), random.randint(0, 8)  # chooses a random coordinate on the board
            if self.board[i][j] != 0:
                self.board[i][j] = 0
                counter -= 1
            else:
                continue
        pass


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    solution = [row[:] for row in sudoku.board]
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board, solution
>>>>>>> origin/main
