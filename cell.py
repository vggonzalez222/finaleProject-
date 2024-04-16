import pygame, sys

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value  # The permanent value of the cell, 0 if empty
        self.sketched_value = None  # Temporary user input value
        self.row = row  # Row position of the cell in the Sudoku grid
        self.col = col  # Column position of the cell in the Sudoku grid
        self.screen = screen  # PyGame screen object to draw the cell
        self.selected = False  # Indicates if the cell is currently selected

    def set_cell_value(self, value):
        """Sets the cell's permanent value."""
        self.value = value

    def set_sketched_value(self, value):
        """Sets the cell's temporary sketched value."""
        self.sketched_value = value

    def draw(self):
        """Draws the cell on the PyGame screen."""
        font = pygame.font.Font(None, 40)  # Set the font and size
        gap = 50  # Size of the cell
        x = self.col * gap
        y = self.row * gap

        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), (x, y, gap, gap), 3)  # Draw red outline if selected
        else:
            pygame.draw.rect(self.screen, (0, 0, 0), (x, y, gap, gap), 1)  # Draw black outline otherwise

        text_color = (0, 0, 0)  # Default text color for numbers
        if self.value != 0:
            # Display the permanent value
            value_surf = font.render(str(self.value), True, text_color)
            self.screen.blit(value_surf, (x + 15, y + 10))
        elif self.sketched_value is not None:
            # Display the sketched value in a smaller font
            sketched_surf = font.render(str(self.sketched_value), True, text_color)
            self.screen.blit(sketched_surf, (x + 5, y + 5))
