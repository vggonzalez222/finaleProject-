import pygame
from constants import *

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.set_sketched_value = 0
        self.width = WIDTH
        self.height = HEIGHT


    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.set_sketched_value = value

    def draw(self):
        #Setting font 
        number_font = pygame.font.Font(None, 60)  # FONT SIZE -  CHANGE LATER
        number_surf = number_font.render(str(self.value), 0, FONT_COLOR)  # SETS FONT COLOR
        emptycell_surf = number_font.render(" ", 0, FONT_COLOR)  # Sets empty cell space

        # Outlines the cell in red if selected
        if pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(self.screen, RED,
            pygame.Rect(self.col * SQUARE_SIZE, self.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), LINE_WIDTH)

        # If cell has NON zero, value is displayed
        if self.value != 0:
            number_rect = number_surf.get_rect(center=(self.col * SQUARE_SIZE + SQUARE_SIZE / 2,
                                                       self.row * SQUARE_SIZE + SQUARE_SIZE / 2))
            self.screen.blit(number_surf, number_rect)  # puts on screen

        # If cell has zero, value is NOT displayed
        elif self.value == 0:
            number_rect = emptycell_surf.get_rect(center=(self.col * SQUARE_SIZE + SQUARE_SIZE / 2,
                                                          self.row * SQUARE_SIZE + SQUARE_SIZE / 2))
            self.screen.blit(emptycell_surf, number_rect)

