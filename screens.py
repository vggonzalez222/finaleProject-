from constants import *
import pygame
import sys


def game_over_screen():
    pygame.init()

    # Set up the screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Load background image
    background = pygame.image.load("background.jpeg")

    # Fill the screen with the background image
    screen.blit(background, (0, 0))

    # Font sizes
    GAME_OVER_SIZE =70
    BUTTON_SIZE = 35

    # Game over text
    game_over_text = "Game Over!"
    game_over_font = pygame.font.Font(None, GAME_OVER_SIZE)
    game_over_surf = game_over_font.render(game_over_text, 0, FONT_COLOR)
    game_over_rect = game_over_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(game_over_surf, game_over_rect)

    # Restart button
    restart_text = "Restart"
    restart_font = pygame.font.Font(None, BUTTON_SIZE)
    restart_surf = restart_font.render(restart_text, 0, FONT_COLOR)
    restart_rect = restart_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
    screen.blit(restart_surf, restart_rect)

    # Update the display
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if restart_rect.collidepoint(x, y):
                    return 'restart'

def game_win_screen():
    pygame.init()

    # Set up the screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Load background image
    background = pygame.image.load("background.jpeg")

    # Fill the screen with the background image
    screen.blit(background, (0, 0))

    # Font sizes
    GAME_OVER_SIZE = 50
    BUTTON_SIZE = 35

    # Game win text
    game_win_text = "Congratulations! You Won!"
    game_over_font = pygame.font.Font(None, GAME_OVER_SIZE)
    game_over_surf = game_over_font.render(game_win_text, 0, FONT_COLOR)
    game_over_rect = game_over_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(game_over_surf, game_over_rect)

    # Exit button
    exit_text = "Exit"
    exit_font = pygame.font.Font(None, BUTTON_SIZE)
    exit_surf = exit_font.render(exit_text, 0, FONT_COLOR)
    exit_rect = exit_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
    screen.blit(exit_surf, exit_rect)

    # Update the display
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if exit_rect.collidepoint(x, y):
                    pygame.quit()
                    sys.exit()