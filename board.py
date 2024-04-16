import pygame, sys
import random
from cell import *  # Assuming you have a Cell class defined as previously described

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cells = [[Cell(0, i, j, self.screen) for j in range(9)] for i in range(9)]
        self.original_state = [[0] * 9 for _ in range(9)]  # To keep track of the initial numbers set when the game starts
        self.selected_cell = None
        #self.remove_cells()

    # def initialize_board():
    #     # 1st approach
    #     return [["-" for i in range(3)] for j in range(3)]
    def draw(self):
        # Draw the board grid
        for i in range(10):
            if i % 3 == 0:
                line_thickness = 4
            else:
                line_thickness = 1
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * (self.height / 9)), (self.width, i * (self.height / 9)), line_thickness)
            pygame.draw.line(self.screen, (0, 0, 0), (i * (self.width / 9), 0), (i * (self.width / 9), self.height), line_thickness)

        # Draw each cell
        for row in self.cells:
            for cell in row:
                cell.draw()


    def select(self, row, col):
        """Marks the cell at (row, col) as the currently selected cell."""
        if self.selected_cell is not None:
            # Deselect the previously selected cell
            self.cells[self.selected_cell[0]][self.selected_cell[1]].selected = False

        self.selected_cell = (row, col)  # Update the currently selected cell
        self.cells[row][col].selected = True  # Mark the new cell as selected

    def click(self, x, y):
        if x < self.width and y < self.height:
            col = x // (self.width // 9)
            row = y // (self.height // 9)
            self.selected_cell = (row, col)
            return (row, col)
        return None


    def clear(self):
        """Clears the value or sketched value of the currently selected cell."""
        if self.selected_cell is not None:
            row, col = self.selected_cell
            cell = self.cells[row][col]
            # Allow clearing if the cell's value was not part of the original puzzle (i.e., it was filled by the user)
            if cell.value == 0:
                cell.set_sketched_value(None)  # Clear any sketched value
            else:
                print("Cannot clear this cell: Original puzzle value.")

    def sketch(self, value):
        """Sets the sketched value of the currently selected cell to the user-entered value."""
        if self.selected_cell is not None:
            row, col = self.selected_cell
            cell = self.cells[row][col]
            # Check if the cell is empty to allow sketching
            if cell.value == 0:
                cell.set_sketched_value(value)
            else:
                print("Cannot sketch in this cell: Permanent value already set.")

    def place_number(self, value):
        """Sets the value of the currently selected cell to the user-entered value, confirming the input."""
        if self.selected_cell is not None:
            row, col = self.selected_cell
            cell = self.cells[row][col]
            # Ensure that the cell is empty before placing a number
            if cell.value == 0:  # Only allow placing numbers in empty cells
                # Optionally, check if the number is valid for the current state of the board
                # This can be done by integrating a method that checks row, column, and box constraints
                if self.is_valid(row, col, value):  # Assuming a method exists to validate the number
                    cell.set_cell_value(value)
                    cell.set_sketched_value(None)  # Clear any sketched value
                else:
                    print("Invalid move: This number violates Sudoku rules.")
            else:
                print("Cannot place a number in this cell: Permanent value already set.")

    def is_valid(self, row, col, num):
        """Checks if placing the number 'num' at (row, col) is valid according to Sudoku rules."""
        # Implement Sudoku rule checks here (row, column, and 3x3 box checks)
        # Check the row
        if any(num == self.cells[row][j].value for j in range(9) if j != col):
            return False
        # Check the column
        if any(num == self.cells[i][col].value for i in range(9) if i != row):
            return False
        # Check the box
        box_row_start = (row // 3) * 3
        box_col_start = (col // 3) * 3
        for i in range(box_row_start, box_row_start + 3):
            for j in range(box_col_start, box_col_start + 3):
                if self.cells[i][j].value == num and (i, j) != (row, col):
                    return False
        return True  # Placeholder for validation logic



    def setup_board(self):
        """Sets up the board with initial clues based on the selected difficulty."""
        # To call a Sudoku puzzle generator
        # For demonstration, this will randomly place numbers according to difficulty
        empty_cells = {
            'easy': 20,  # 20 numbers filled, 61 empty
            'medium': 30,  # 30 numbers filled, 51 empty
            'hard': 40  # 40 numbers filled, 41 empty
        }

        # Generate a full valid Sudoku solution first
        self.generate_full_solution()

        # Remove cells to create the puzzle
        num_filled = empty_cells[self.difficulty]
        filled_positions = set()
        while len(filled_positions) < num_filled:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if (row, col) not in filled_positions:
                filled_positions.add((row, col))

        # Setup initial board state based on filled positions
        for i in range(9):
            for j in range(9):
                if (i, j) in filled_positions:
                    self.cells[i][j].set_cell_value(self.original_state[i][j])
                else:
                    self.cells[i][j].set_cell_value(0)
                    self.original_state[i][j] = 0

    def generate_full_solution(self):
        """Generates a full valid Sudoku board (not implemented here)."""
        # You need to implement this method based on Sudoku generation logic.
        # For demonstration, assuming it fills self.original_state with a valid solution.
        for i in range(9):
            for j in range(9):
                # This should actually be the result of a proper Sudoku solution generation algorithm
                self.original_state[i][j] = (i * 3 + i // 3 + j) % 9 + 1


    def reset_to_original(self):
        """Resets all cells to their original values (clues)."""
        for i in range(9):
            for j in range(9):
                original_value = self.original_state[i][j]
                self.cells[i][j].set_cell_value(original_value)
                self.cells[i][j].set_sketched_value(None)  # Clear any sketched values
                self.cells[i][j].selected = False  # Deselect any cell if selected

        if self.selected_cell is not None:
            self.cells[self.selected_cell[0]][self.selected_cell[1]].selected = False
            self.selected_cell = None  # Clear selection


    def is_full(self):
        """Checks if all cells on the board are filled with non-zero values."""
        for row in self.cells:
            for cell in row:
                if cell.value == 0:  # If any cell is empty
                    return False
        return True

    def update_board(self):
        """Updates the visual representation of the board based on the current cell states."""
        for i in range(9):
            for j in range(9):
                cell = self.cells[i][j]
                cell.draw()  # Assuming each Cell object has a draw method that updates its appearance on the screen

        pygame.display.update()  # Update the entire screen to reflect changes

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.cells[i][j].value == 0:# Checking if the cell value is 0 which indicates it's empty
                    return (i, j)  # row, col # Return the position of the empty cell
        return None # No empty cell was found

    # if the board was solved correctly
    def check_board(self):
        for row in range(9):
            for col in range(9):
                num = self.cells[row][col].value
                if num == 0 or not self.is_valid(row, col, num):
                    return False
        return True