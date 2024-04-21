import pygame
import sys
from constants import *
from board import Board
from cell import Cell
from sudoku_generator import SudokuGenerator

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")


def welcome_screen():

    # Loads in background image
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    background = pygame.image.load("background.jpg")
    screen.blit(background, (-30,-20))
    pygame.display.update()

    # Font sizes
    WELCOME_SIZE = 70
    MODE_SIZE = 45
    DIFFICULTY_SIZE = 35

    # Welcome Outline


    # Welcome to Sudoku text
    welcome_text = "Welcome to Sudoku"
    welcome_font = pygame.font.Font(None, WELCOME_SIZE)
    welcome_surf = welcome_font.render(welcome_text, 0, BLACK)
    welcome_rect = welcome_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 140))
    screen.blit(welcome_surf, welcome_rect)


    # Select Game Mode text
    Mode_text = "Select Game Mode:"
    Mode_font = pygame.font.Font(None, MODE_SIZE)
    Mode_surf = Mode_font.render(Mode_text, 0, BLACK)
    Mode_rect = Mode_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))
    screen.blit(Mode_surf, Mode_rect)

    # easy text outline
    easy_width = 110
    easy_height = 40
    easy_x = 145
    easy_y = HEIGHT // 2 + 30
    easy_rect_outline = pygame.Rect(easy_x, easy_y, easy_width, easy_height)
    pygame.draw.rect(screen, GREEN, easy_rect_outline)


    # easy text
    easy_text = "EASY"
    easy_font = pygame.font.Font(None, DIFFICULTY_SIZE)
    easy_surf = easy_font.render(easy_text, 0, BG_COLOR)
    easy_rect = easy_surf.get_rect(center=(200, HEIGHT // 2 + 50))
    screen.blit(easy_surf, easy_rect)

    # medium text outline
    medium_width = 110
    medium_height = 40
    medium_x = 345
    medium_y = HEIGHT // 2 + 30
    medium_rect_outline = pygame.Rect(medium_x, medium_y, medium_width, medium_height)
    pygame.draw.rect(screen, ORANGE, medium_rect_outline)

    # medium text
    medium_text = "MEDIUM"
    medium_font = pygame.font.Font(None, DIFFICULTY_SIZE)
    medium_surf = medium_font.render(medium_text, 0, BG_COLOR)
    medium_rect = medium_surf.get_rect(center=(400, HEIGHT // 2 + 50))
    screen.blit(medium_surf, medium_rect)

    # hard text outline
    hard_width = 110
    hard_height = 40
    hard_x = 545
    hard_y = HEIGHT // 2 + 30
    hard_rect_outline = pygame.Rect(hard_x, hard_y, hard_width, hard_height)
    pygame.draw.rect(screen, RED, hard_rect_outline)

    # hard text
    hard_text = "HARD"
    hard_font = pygame.font.Font(None, DIFFICULTY_SIZE)
    hard_surf = hard_font.render(hard_text, 0, BG_COLOR)
    hard_rect = hard_surf.get_rect(center=(600, HEIGHT // 2 + 50))
    screen.blit(hard_surf, hard_rect)

    # Difficulty Buttons

    while True:
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # returns difficulty type string when clicked on
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rect_outline.collidepoint(event.pos):
                    return 'easy'

                if medium_rect_outline.collidepoint(event.pos):
                    return 'medium'

                if hard_rect_outline.collidepoint(event.pos):
                    return 'hard'

        pygame.display.update()

welcome_screen()
