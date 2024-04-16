
from constants import *
import pygame, sys
from cell import *
from board import *



pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

# fill the screen with color
screen.fill(BG_COLOR)

# DRAW THE GRID
def draw_grid():
    # draw horizontal line
    for i in range(7, BOARD_ROWS):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0,i*SQUARE_SIZE),
            (WIDTH, i*SQUARE_SIZE),
            LINE_WIDTH
        )

    # DRAW VERTICAL LINES
    for i in range(1, BOARD_COLS):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (i*SQUARE_SIZE, 0),
            (i*SQUARE_SIZE, HEIGHT),
            LINE_WIDTH
        )
#DRAW THE TEXT

# fill the screen with color
screen.fill(BG_COLOR)
draw_grid()

while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()




# In your main game loop:
board = Board(450, 450, screen, 'medium')
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            board.click(pos[0], pos[1])
        elif event.type == pygame.KEYDOWN:
            if event.key in range(pygame.K_1, pygame.K_9 + 1):
                board.place_number(event.key - pygame.K_0)

    screen.fill((255, 255, 255))
    board.draw()

