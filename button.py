from makeshift_board import  *
from makeshift_sudoku_project import *
import pygame
from makeshift_board import *
import sys

DIFFICULTIES = {
    'easy': 30,  # 30 cells will be empty
    'medium': 40,  # 40 cells will be empty
    'hard': 50  # 50 cells will be empty
}
def draw_buttons(screen):
    # This is a simple representation. You would use pygame.draw and label the buttons
    easy_button = pygame.Rect(100, 100, 100, 50)  # x, y, width, height
    medium_button = pygame.Rect(250, 100, 100, 50)
    hard_button = pygame.Rect(400, 100, 100, 50)
    pygame.draw.rect(screen, [255, 0, 0], easy_button)  # Red button for easy
    pygame.draw.rect(screen, [0, 255, 0], medium_button)  # Green button for medium
    pygame.draw.rect(screen, [0, 0, 255], hard_button)  # Blue button for hard
    return easy_button, medium_button, hard_button

def handle_button_click(pos, buttons):
    easy_button, medium_button, hard_button = buttons
    if easy_button.collidepoint(pos):
        start_game('easy')
    elif medium_button.collidepoint(pos):
        start_game('medium')
    elif hard_button.collidepoint(pos):
        start_game('hard')


def start_game(difficulty):
    empty_cells = DIFFICULTIES[difficulty]
    # Assuming `generate_sudoku` is a function that creates the board and handles logic
    board = generate_sudoku(9, empty_cells)  # 9x9 Sudoku with specified empty cells
    # Further logic to display or reset the game state



